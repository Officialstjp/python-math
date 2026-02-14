---
description: This file describes the coding style and environment setup for the Math Repository.
applyTo: '**/*.py, **/*.ipynb'
---
# Math Repository

When working with Python code in this repository, please adhere to the following coding rules:
1. Use meaningful variable and function names that clearly describe their purpose.
2. Include comments to explain complex logic and important sections of the code.
3. Split up according to relationship and context: Notebooks should follow a linear narrative of good mixes.
4. Extract configuration from implementation: Any configuration should be in separate cells to allow for an easier user experience.

Furthermore, a venv is used for this repository. To set up the environment, run the following commands in your terminal:
```powershell
.\venv\Scripts\activate
```
Only then, try to run the code. This ensures that all dependencies are properly installed and available for use.

---

When working with Jupyter Notebooks, please ensure that you follow the same coding rules as outlined above. Additionally, make sure to organize your notebooks in a way that tells a clear and coherent story, making it easier for others to understand the flow of your work. Ensure to follow the theme of other notebooks in the repository to maintain general consistency, and the theme of similar notebooks to maintain consistency in depth, breadth, and style (e.g., if a notebook is more of a tutorial, it should be more detailed and include more explanations than a notebook that is more of an exploration; a foundational math Notebook should provide simple explanations and examples, while an experiments and research notebooks can be more complex and detailed).
