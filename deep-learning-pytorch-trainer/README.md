# 🔥 Deep Learning: PyTorch Foundations & Modular Trainer

[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Python](https://img.shields.io/badge/Python-Jupyter-F37626.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)

A deep learning sequence illustrating the journey from fundamental tensor operations and manual gradient calculus up to object-oriented multi-layer perceptron (MLP) architectures and an extensible `Trainer` class.

---

## 🔬 Coursework Progression

1. **`01_pytorch_tensors_autograd.ipynb`**:
   - PyTorch tensor manipulation, broadcasting, memory layouts, and automatic differentiation (`loss.backward()`).
2. **`02_manual_backprop_optimization.ipynb`**:
   - Explicit manual derivation and code implementation of partial derivatives ($\frac{\partial L}{\partial w}$, $\frac{\partial L}{\partial b}$) without using high-level modules.
   - Parameter update step mechanics.
3. **`03_modular_mlp_trainer_benchmarks.ipynb`**:
   - Transition to `torch.nn.Module`, hidden linear layers with non-linear activations (ReLU).
   - Implementation of an OOP `Trainer` harness with epoch callbacks and validation loss monitoring.
   - Empirical convergence comparison between **SGD**, **SGD + Momentum**, and **Adam**.

