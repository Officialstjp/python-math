[CmdletBinding()]
param(
    [ValidateSet("Foundations", "ml")]
    [string[]]$Target = @("Foundations", "ml"),

    [ValidateSet("html", "markdown", "pdf")]
    [string[]]$Formats = @("html", "markdown", "pdf"),

    [string]$Config,

    [Nullable[int]]$Workers = $null,

    [switch]$IncludeExercises,

    [switch]$NoTextOutput,

    # Export all content (exercises, text output, glossary) into exports_full/.
    # Automatically uses scripts/export_profile_full.toml when no -Config is given.
    [switch]$FullContent
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Resolve-Path (Join-Path $scriptDir "..")
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"
$pythonExe = if (Test-Path $venvPython) { $venvPython } else { "python" }

$targetPresets = [ordered]@{
    Foundations = [ordered]@{
        SourceDir        = "Foundations"
        OutputDir        = "exports/Foundations"
        FullOutputDir    = "exports_full/Foundations"
        Title            = "Mathematik Grundlagen"
        FullTitle        = "Mathematik Foundations (vollständig)"
        PdfOutputName    = "Foundations_reference.pdf"
        FullPdfOutputName = "Foundations_full.pdf"
        HtmlOutputName   = "Foundations_reference.html"
        FullHtmlOutputName = "Foundations_full.html"
    }
    ml = [ordered]@{
        SourceDir        = "ml"
        OutputDir        = "exports/ml"
        FullOutputDir    = "exports_full/ml"
        Title            = "Machine-Learning Referenz"
        FullTitle        = "Machine-Learning Referenz (vollständig)"
        PdfOutputName    = "ML_reference.pdf"
        FullPdfOutputName = "ML_full.pdf"
        HtmlOutputName   = "ML_reference.html"
        FullHtmlOutputName = "ML_full.html"
    }
}

$selectedTargets = @()
foreach ($name in $Target) {
    if ($selectedTargets -notcontains $name) {
        $selectedTargets += $name
    }
}

$selectedFormats = @()
foreach ($format in $Formats) {
    if ($selectedFormats -notcontains $format) {
        $selectedFormats += $format
    }
}

$configArgs = @()
if ($Config) {
    $resolvedConfig = if ([System.IO.Path]::IsPathRooted($Config)) {
        $Config
    }
    else {
        Join-Path $repoRoot $Config
    }

    if (-not (Test-Path $resolvedConfig -PathType Leaf)) {
        throw ('Config file not found: ' + $resolvedConfig)
    }

    $configArgs = @("--config", $resolvedConfig)
}
elseif ($FullContent) {
    # Auto-use the full profile when -FullContent is set and no explicit config is given.
    $fullProfilePath = Join-Path $scriptDir "export_profile_full.toml"
    if (Test-Path $fullProfilePath -PathType Leaf) {
        $configArgs = @("--config", $fullProfilePath)
        Write-Host "Using full-content profile: $fullProfilePath" -ForegroundColor DarkCyan
    }
}

function Invoke-ExportStep {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Label,

        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    Write-Host "== $Label ==" -ForegroundColor Cyan
    & $pythonExe @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw ('Command failed with exit code ' + $LASTEXITCODE + ' - ' + $Label)
    }
    Write-Host ""
}

Push-Location $repoRoot
try {
    foreach ($name in $selectedTargets) {
        $preset = $targetPresets[$name]

        # Select output dirs and titles depending on whether full-content mode is active.
        $outputDir   = if ($FullContent) { $preset.FullOutputDir }    else { $preset.OutputDir }
        $title       = if ($FullContent) { $preset.FullTitle }         else { $preset.Title }
        $pdfName     = if ($FullContent) { $preset.FullPdfOutputName } else { $preset.PdfOutputName }
        $htmlName    = if ($FullContent) { $preset.FullHtmlOutputName } else { $preset.HtmlOutputName }

        $exportArgs = @("scripts/export_notebooks.py") +
            $configArgs +
            @("--formats") +
            $selectedFormats +
            @(
                "--source-dir", $preset.SourceDir,
                "--output-dir", $outputDir
            )

        if ($null -ne $Workers) {
            $exportArgs += @("--workers", "$Workers")
        }

        # In full-content mode exercises are always included; otherwise default to excluding them.
        if (-not $FullContent -and -not $IncludeExercises) {
            $exportArgs += "--no-exercises"
        }
        if (-not $FullContent -and $NoTextOutput) {
            $exportArgs += "--no-text-output"
        }

        Invoke-ExportStep -Label "$name exports" -Arguments $exportArgs

        if ($selectedFormats -contains "pdf") {
            Invoke-ExportStep -Label "$name consolidated PDF" -Arguments (
                @("scripts/consolidate_pdfs.py") +
                $configArgs +
                @(
                    "--pdf-dir", "$outputDir/pdf",
                    "--output-dir", "$outputDir/pdf",
                    "--title", $title,
                    "--output-name", $pdfName
                )
            )
        }

        if ($selectedFormats -contains "html") {
            Invoke-ExportStep -Label "$name consolidated HTML" -Arguments (
                @("scripts/consolidate_htmls.py") +
                $configArgs +
                @(
                    "--html-dir", "$outputDir/html",
                    "--output-dir", "$outputDir/html",
                    "--title", $title,
                    "--output-name", $htmlName
                )
            )
        }
    }
}
finally {
    Pop-Location
}