from dataclasses import dataclass
import sys

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider


@dataclass(frozen=True)
class AttentionLabConfig:
    prompt_tokens: tuple[str, ...] = (
        "<BOS>",
        "wir",
        "visualisieren",
        "attention",
        "zwischen",
        "tokens",
        "im",
        "hochdimensionalen",
        "raum",
        "und",
        "sagen",
        "das",
        "naechste",
        "token",
    )
    vocabulary_tokens: tuple[str, ...] = (
        "<BOS>",
        "wir",
        "visualisieren",
        "attention",
        "zwischen",
        "tokens",
        "im",
        "hochdimensionalen",
        "raum",
        "und",
        "sagen",
        "das",
        "naechste",
        "token",
        "modell",
        "lernt",
        "muster",
        "matrix",
        "kontext",
        "wahrscheinlichkeit",
        "prediction",
        "embedding",
        "daten",
        "gradient",
        "funktion",
        "idee",
        "experiment",
        "kurve",
        "dimension",
        "verteilung",
    )
    semantic_axes: tuple[str, ...] = (
        "syntax",
        "math",
        "code",
        "data",
        "model",
        "memory",
        "uncertainty",
        "time",
        "logic",
        "visual",
        "learning",
        "prediction",
        "attention",
        "context",
        "scale",
        "cause",
        "abstract",
        "play",
    )
    seed: int = 42
    attention_sharpness: float = 1.45
    prediction_temperature: float = 0.85
    top_prediction_count: int = 9
    top_dimension_count: int = 10
    figure_size: tuple[float, float] = (16, 9)


@dataclass
class AttentionModelState:
    config: AttentionLabConfig
    vocabulary: tuple[str, ...]
    token_to_index: dict[str, int]
    sequence_indices: np.ndarray
    vocabulary_embeddings: np.ndarray
    sequence_embeddings: np.ndarray
    query_matrix: np.ndarray
    key_matrix: np.ndarray
    value_matrix: np.ndarray
    transition_bias: np.ndarray
    sequence_projection: np.ndarray


def softmax(values, temperature=1.0, axis=-1):
    temperature = max(float(temperature), 1e-6)
    scaled_values = values / temperature
    scaled_values = scaled_values - np.max(scaled_values, axis=axis, keepdims=True)
    exp_values = np.exp(scaled_values)
    return exp_values / np.sum(exp_values, axis=axis, keepdims=True)


def normalize(matrix, axis=-1):
    norms = np.linalg.norm(matrix, axis=axis, keepdims=True)
    return matrix / np.maximum(norms, 1e-9)


def pca_projection(matrix, components=2):
    centered_matrix = matrix - matrix.mean(axis=0, keepdims=True)
    _, _, right_singular_vectors = np.linalg.svd(centered_matrix, full_matrices=False)
    return centered_matrix @ right_singular_vectors[:components].T


def random_rotation(dimension_count, random_generator):
    raw_matrix = random_generator.normal(size=(dimension_count, dimension_count))
    orthogonal_matrix, _ = np.linalg.qr(raw_matrix)
    return orthogonal_matrix


def make_semantic_vector(axis_index, **weights):
    vector = np.zeros(len(axis_index), dtype=float)
    for axis_name, weight in weights.items():
        vector[axis_index[axis_name]] = weight
    return vector


def semantic_weights(axis_index):
    return {
        "<BOS>": make_semantic_vector(axis_index, syntax=1.2, context=0.8, memory=0.4),
        "wir": make_semantic_vector(axis_index, syntax=1.0, context=0.8, play=0.3),
        "visualisieren": make_semantic_vector(axis_index, visual=1.8, code=0.6, math=0.5, play=0.5),
        "attention": make_semantic_vector(axis_index, attention=2.1, model=1.4, prediction=0.8, context=1.0),
        "zwischen": make_semantic_vector(axis_index, syntax=1.0, logic=0.8, context=0.7),
        "tokens": make_semantic_vector(axis_index, code=0.9, model=0.8, attention=0.8, data=0.8),
        "im": make_semantic_vector(axis_index, syntax=1.1, context=0.5),
        "hochdimensionalen": make_semantic_vector(axis_index, math=1.4, abstract=1.4, scale=1.1),
        "raum": make_semantic_vector(axis_index, visual=0.9, math=1.1, abstract=1.0, scale=0.8),
        "und": make_semantic_vector(axis_index, syntax=1.1, context=0.5),
        "sagen": make_semantic_vector(axis_index, prediction=1.0, syntax=0.7, cause=0.5),
        "das": make_semantic_vector(axis_index, syntax=1.0, context=0.4),
        "naechste": make_semantic_vector(axis_index, prediction=1.6, time=0.9, uncertainty=0.5),
        "token": make_semantic_vector(axis_index, prediction=1.1, model=0.8, attention=0.8, code=0.7),
        "modell": make_semantic_vector(axis_index, model=1.9, learning=1.0, prediction=0.7),
        "lernt": make_semantic_vector(axis_index, learning=1.8, model=1.2, cause=0.7),
        "muster": make_semantic_vector(axis_index, logic=1.1, data=1.1, learning=1.0, visual=0.4),
        "matrix": make_semantic_vector(axis_index, math=1.5, code=0.8, attention=0.8, abstract=0.8),
        "kontext": make_semantic_vector(axis_index, context=2.0, memory=1.1, attention=0.9),
        "wahrscheinlichkeit": make_semantic_vector(axis_index, uncertainty=1.7, math=1.1, prediction=1.0),
        "prediction": make_semantic_vector(axis_index, prediction=2.1, model=1.1, uncertainty=0.9),
        "embedding": make_semantic_vector(axis_index, model=1.1, math=1.0, code=0.8, abstract=1.2),
        "daten": make_semantic_vector(axis_index, data=1.9, learning=0.7, model=0.5),
        "gradient": make_semantic_vector(axis_index, learning=1.2, math=1.2, cause=0.7, code=0.6),
        "funktion": make_semantic_vector(axis_index, math=1.3, logic=0.9, code=0.4),
        "idee": make_semantic_vector(axis_index, abstract=1.0, play=0.8, context=0.6),
        "experiment": make_semantic_vector(axis_index, play=1.1, code=0.9, visual=0.7, learning=0.7),
        "kurve": make_semantic_vector(axis_index, visual=1.3, math=1.0),
        "dimension": make_semantic_vector(axis_index, math=1.1, abstract=1.4, scale=0.9),
        "verteilung": make_semantic_vector(axis_index, math=1.2, uncertainty=1.4, data=0.8),
    }


def create_vocabulary_embeddings(config):
    random_generator = np.random.default_rng(config.seed)
    axis_index = {axis_name: index for index, axis_name in enumerate(config.semantic_axes)}
    base_vectors = semantic_weights(axis_index)

    embeddings = []
    for token in config.vocabulary_tokens:
        base_vector = base_vectors[token].copy()
        texture_noise = random_generator.normal(scale=0.13, size=len(config.semantic_axes))
        embeddings.append(base_vector + texture_noise)

    return normalize(np.vstack(embeddings))


def create_transition_bias(vocabulary, token_to_index):
    transition_bias = np.zeros((len(vocabulary), len(vocabulary)), dtype=float)
    transition_rules = (
        ("<BOS>", "wir", 2.0),
        ("wir", "visualisieren", 1.4),
        ("visualisieren", "attention", 1.7),
        ("attention", "matrix", 1.4),
        ("attention", "zwischen", 1.2),
        ("tokens", "im", 1.2),
        ("hochdimensionalen", "raum", 1.8),
        ("raum", "und", 1.2),
        ("sagen", "das", 1.4),
        ("das", "naechste", 1.7),
        ("naechste", "token", 2.0),
        ("token", "prediction", 2.4),
        ("token", "wahrscheinlichkeit", 1.6),
        ("token", "embedding", 1.1),
        ("modell", "lernt", 1.6),
        ("lernt", "muster", 1.6),
        ("muster", "aus", 1.0),
        ("embedding", "raum", 1.3),
        ("matrix", "kontext", 1.4),
        ("kontext", "prediction", 1.2),
        ("wahrscheinlichkeit", "verteilung", 1.5),
    )

    for source_token, target_token, weight in transition_rules:
        if source_token in token_to_index and target_token in token_to_index:
            transition_bias[token_to_index[source_token], token_to_index[target_token]] += weight

    return transition_bias


def create_model_state(config):
    random_generator = np.random.default_rng(config.seed + 100)
    vocabulary = config.vocabulary_tokens
    token_to_index = {token: index for index, token in enumerate(vocabulary)}
    sequence_indices = np.array([token_to_index[token] for token in config.prompt_tokens], dtype=int)
    vocabulary_embeddings = create_vocabulary_embeddings(config)
    sequence_embeddings = vocabulary_embeddings[sequence_indices]

    dimension_count = len(config.semantic_axes)
    query_matrix = 0.82 * np.eye(dimension_count) + 0.18 * random_rotation(dimension_count, random_generator)
    key_matrix = 0.78 * np.eye(dimension_count) + 0.22 * random_rotation(dimension_count, random_generator)
    value_matrix = 0.88 * np.eye(dimension_count) + 0.12 * random_rotation(dimension_count, random_generator)

    return AttentionModelState(
        config=config,
        vocabulary=vocabulary,
        token_to_index=token_to_index,
        sequence_indices=sequence_indices,
        vocabulary_embeddings=vocabulary_embeddings,
        sequence_embeddings=sequence_embeddings,
        query_matrix=query_matrix,
        key_matrix=key_matrix,
        value_matrix=value_matrix,
        transition_bias=create_transition_bias(vocabulary, token_to_index),
        sequence_projection=pca_projection(sequence_embeddings),
    )


def calculate_attention(state, attention_sharpness):
    query_vectors = state.sequence_embeddings @ state.query_matrix
    key_vectors = state.sequence_embeddings @ state.key_matrix
    value_vectors = state.sequence_embeddings @ state.value_matrix

    raw_scores = (query_vectors @ key_vectors.T) / np.sqrt(query_vectors.shape[1])
    raw_scores = raw_scores * attention_sharpness

    causal_mask = np.triu(np.ones_like(raw_scores, dtype=bool), k=1)
    masked_scores = np.where(causal_mask, -1e9, raw_scores)
    attention_weights = softmax(masked_scores, axis=1)
    context_vectors = attention_weights @ value_vectors

    return masked_scores, attention_weights, context_vectors


def predict_next_tokens(state, context_vector, current_vocabulary_index, temperature):
    output_vectors = normalize(state.vocabulary_embeddings @ state.value_matrix)
    context_direction = normalize(context_vector.reshape(1, -1))[0]
    logits = output_vectors @ context_direction * np.sqrt(output_vectors.shape[1])
    logits = logits + state.transition_bias[current_vocabulary_index]

    if state.vocabulary[current_vocabulary_index] != "<BOS>":
        logits[state.token_to_index["<BOS>"]] -= 4.0

    probabilities = softmax(logits, temperature=temperature)
    return probabilities


class AttentionLab:
    def __init__(self, config):
        self.state = create_model_state(config)
        self.figure = plt.figure(figsize=config.figure_size)
        self.figure.canvas.manager.set_window_title("Transformer Attention Lab")
        self.figure.subplots_adjust(left=0.06, right=0.98, top=0.91, bottom=0.22, wspace=0.42, hspace=0.5)

        grid = self.figure.add_gridspec(2, 3, width_ratios=[1.28, 1.05, 1.05], height_ratios=[1, 1])
        self.space_axis = self.figure.add_subplot(grid[:, 0])
        self.heatmap_axis = self.figure.add_subplot(grid[0, 1])
        self.attention_axis = self.figure.add_subplot(grid[1, 1])
        self.prediction_axis = self.figure.add_subplot(grid[0, 2])
        self.dimension_axis = self.figure.add_subplot(grid[1, 2])

        self.position_slider = Slider(
            ax=self.figure.add_axes([0.12, 0.13, 0.62, 0.026]),
            label="Query-Position",
            valmin=0,
            valmax=len(config.prompt_tokens) - 1,
            valinit=len(config.prompt_tokens) - 1,
            valstep=1,
        )
        self.temperature_slider = Slider(
            ax=self.figure.add_axes([0.12, 0.085, 0.62, 0.026]),
            label="Prediction-Temperatur",
            valmin=0.25,
            valmax=2.5,
            valinit=config.prediction_temperature,
        )
        self.sharpness_slider = Slider(
            ax=self.figure.add_axes([0.12, 0.04, 0.62, 0.026]),
            label="Attention-Schaerfe",
            valmin=0.25,
            valmax=3.5,
            valinit=config.attention_sharpness,
        )
        self.reset_button = Button(
            ax=self.figure.add_axes([0.79, 0.06, 0.13, 0.065]),
            label="Reset",
        )

        self.position_slider.on_changed(self.update)
        self.temperature_slider.on_changed(self.update)
        self.sharpness_slider.on_changed(self.update)
        self.reset_button.on_clicked(self.reset)
        self.figure.canvas.mpl_connect("button_press_event", self.select_nearest_token)

        self.update(None)

    def reset(self, _event):
        self.position_slider.reset()
        self.temperature_slider.reset()
        self.sharpness_slider.reset()

    def select_nearest_token(self, event):
        if event.inaxes is not self.space_axis or event.xdata is None or event.ydata is None:
            return

        click_position = np.array([event.xdata, event.ydata])
        distances = np.linalg.norm(self.state.sequence_projection - click_position, axis=1)
        nearest_index = int(np.argmin(distances))
        self.position_slider.set_val(nearest_index)

    def update(self, _event):
        selected_position = int(self.position_slider.val)
        temperature = float(self.temperature_slider.val)
        attention_sharpness = float(self.sharpness_slider.val)

        _, attention_weights, context_vectors = calculate_attention(self.state, attention_sharpness)
        selected_attention = attention_weights[selected_position]
        selected_context = context_vectors[selected_position]
        current_vocabulary_index = self.state.sequence_indices[selected_position]
        probabilities = predict_next_tokens(
            self.state,
            selected_context,
            current_vocabulary_index,
            temperature,
        )

        self.draw_embedding_space(selected_position, selected_attention)
        self.draw_attention_heatmap(selected_position, attention_weights)
        self.draw_attention_bars(selected_position, selected_attention)
        self.draw_prediction_bars(probabilities)
        self.draw_dimension_probe(selected_context)

        current_token = self.state.config.prompt_tokens[selected_position]
        self.figure.suptitle(
            f"Transformer Attention Lab: query='{current_token}' | hidden space={len(self.state.config.semantic_axes)}D",
            fontsize=16,
        )
        self.figure.canvas.draw_idle()

    def draw_embedding_space(self, selected_position, selected_attention):
        self.space_axis.clear()
        coordinates = self.state.sequence_projection
        tokens = self.state.config.prompt_tokens

        self.space_axis.scatter(coordinates[:, 0], coordinates[:, 1], s=90, color="#D8DEE9", edgecolor="#2E3440", zorder=3)
        self.space_axis.scatter(
            coordinates[selected_position, 0],
            coordinates[selected_position, 1],
            s=180,
            color="#BF616A",
            edgecolor="black",
            zorder=6,
        )

        query_coordinate = coordinates[selected_position]
        for token_index in range(selected_position + 1):
            weight = selected_attention[token_index]
            if token_index == selected_position or weight < 0.025:
                continue
            target_coordinate = coordinates[token_index]
            self.space_axis.annotate(
                "",
                xy=target_coordinate,
                xytext=query_coordinate,
                arrowprops=dict(
                    arrowstyle="->",
                    color=(0.18, 0.33, 0.65, min(0.85, 0.18 + weight * 2.6)),
                    linewidth=1.0 + weight * 8.0,
                    shrinkA=10,
                    shrinkB=10,
                ),
                zorder=2,
            )

        for token_index, (x_position, y_position) in enumerate(coordinates):
            label_color = "#BF616A" if token_index == selected_position else "#2E3440"
            self.space_axis.text(x_position + 0.015, y_position + 0.015, tokens[token_index], fontsize=9, color=label_color)

        self.space_axis.axhline(0, color="gray", linewidth=0.7, alpha=0.4)
        self.space_axis.axvline(0, color="gray", linewidth=0.7, alpha=0.4)
        dimension_count = len(self.state.config.semantic_axes)
        self.space_axis.set_title(f"2D-PCA-Schatten des {dimension_count}D Tokenraums", fontsize=12)
        self.space_axis.set_xlabel("PCA 1")
        self.space_axis.set_ylabel("PCA 2")
        self.space_axis.grid(True, alpha=0.18)

    def draw_attention_heatmap(self, selected_position, attention_weights):
        self.heatmap_axis.clear()
        tokens = self.state.config.prompt_tokens
        self.heatmap_axis.imshow(attention_weights, cmap="magma", vmin=0, vmax=max(0.55, attention_weights.max()))
        self.heatmap_axis.axhline(selected_position - 0.5, color="cyan", linewidth=1.5)
        self.heatmap_axis.axhline(selected_position + 0.5, color="cyan", linewidth=1.5)
        self.heatmap_axis.set_title("Causal Attention Matrix")
        self.heatmap_axis.set_xticks(range(len(tokens)))
        self.heatmap_axis.set_yticks(range(len(tokens)))
        self.heatmap_axis.set_xticklabels(tokens, rotation=65, ha="right", fontsize=7)
        self.heatmap_axis.set_yticklabels(tokens, fontsize=7)
        self.heatmap_axis.set_xlabel("Keys: Worauf wird geschaut?")
        self.heatmap_axis.set_ylabel("Queries: Wer schaut?")

    def draw_attention_bars(self, selected_position, selected_attention):
        self.attention_axis.clear()
        tokens = self.state.config.prompt_tokens[: selected_position + 1]
        weights = selected_attention[: selected_position + 1]
        bar_colors = ["#5E81AC"] * len(tokens)
        bar_colors[-1] = "#BF616A"

        self.attention_axis.bar(range(len(tokens)), weights, color=bar_colors, alpha=0.9)
        self.attention_axis.set_ylim(0, max(0.35, weights.max() * 1.2))
        self.attention_axis.set_title("Attention der ausgewaehlten Query")
        self.attention_axis.set_xticks(range(len(tokens)))
        self.attention_axis.set_xticklabels(tokens, rotation=55, ha="right", fontsize=8)
        self.attention_axis.set_ylabel("Gewicht")
        self.attention_axis.grid(True, axis="y", alpha=0.25)

    def draw_prediction_bars(self, probabilities):
        self.prediction_axis.clear()
        top_indices = np.argsort(probabilities)[-self.state.config.top_prediction_count :]
        top_indices = top_indices[np.argsort(probabilities[top_indices])]
        top_tokens = [self.state.vocabulary[index] for index in top_indices]
        top_probabilities = probabilities[top_indices]

        self.prediction_axis.barh(top_tokens, top_probabilities, color="#A3BE8C")
        self.prediction_axis.set_xlim(0, max(0.35, top_probabilities.max() * 1.2))
        self.prediction_axis.set_title("Naechster-Token-Verteilung")
        self.prediction_axis.set_xlabel("Wahrscheinlichkeit")
        self.prediction_axis.grid(True, axis="x", alpha=0.25)

        for token_index, probability in enumerate(top_probabilities):
            self.prediction_axis.text(probability + 0.006, token_index, f"{probability:.2f}", va="center", fontsize=8)

    def draw_dimension_probe(self, context_vector):
        self.dimension_axis.clear()
        axis_names = np.array(self.state.config.semantic_axes)
        top_indices = np.argsort(np.abs(context_vector))[-self.state.config.top_dimension_count :]
        top_indices = top_indices[np.argsort(context_vector[top_indices])]
        top_values = context_vector[top_indices]
        top_names = axis_names[top_indices]
        colors = ["#B48EAD" if value >= 0 else "#D08770" for value in top_values]

        self.dimension_axis.barh(top_names, top_values, color=colors)
        self.dimension_axis.axvline(0, color="black", linewidth=0.8)
        self.dimension_axis.set_title("Context Vector: staerkste Hidden-Dimensionen")
        self.dimension_axis.set_xlabel("Aktivierung")
        self.dimension_axis.grid(True, axis="x", alpha=0.25)

    def show(self):
        print("Transformer Attention Lab")
        print("- Slider bewegen: Query-Position, Prediction-Temperatur, Attention-Schaerfe")
        print("- Auf einen Token im PCA-Raum klicken: Query direkt auswaehlen")
        print("- Fenster schliessen beendet das Experiment")
        plt.show()


def run_smoke_test(config):
    state = create_model_state(config)
    _, attention_weights, context_vectors = calculate_attention(state, config.attention_sharpness)
    selected_position = len(config.prompt_tokens) - 1
    selected_context = context_vectors[selected_position]
    current_vocabulary_index = state.sequence_indices[selected_position]
    probabilities = predict_next_tokens(state, selected_context, current_vocabulary_index, config.prediction_temperature)
    top_indices = np.argsort(probabilities)[-5:][::-1]

    print("Smoke test OK")
    print(f"Sequence length: {len(config.prompt_tokens)}")
    print(f"Hidden dimensions: {len(config.semantic_axes)}")
    print(f"Attention matrix shape: {attention_weights.shape}")
    print("Top next-token predictions:")
    for index in top_indices:
        print(f"  {state.vocabulary[index]:>18s}: {probabilities[index]:.3f}")


def main():
    config = AttentionLabConfig()
    if "--no-show" in sys.argv:
        run_smoke_test(config)
        return

    AttentionLab(config).show()


if __name__ == "__main__":
    main()
