{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1. Introduction to Jupyter Notebooks\n",
    "\n",
    "---\n",
    "\n",
    "**Definition and Utility**\n",
    "\n",
    "Jupyter Notebooks are an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. The name \"Jupyter\" is derived from three programming languages: **Ju**lia, **Pyt**hon, and **R**, though today, the notebook technology supports [many more languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels).\n",
    "\n",
    "**Key Features**\n",
    "\n",
    "- **Interactivity**: Jupyter Notebooks allow users to write and execute code in a step-by-step manner, enabling interactive data exploration and visualization.\n",
    "  \n",
    "- **Multimedia Integration**: Notebooks support mixing in-line text (with full Markdown & LaTeX support), code, and visual outputs, which provides a comprehensive platform to document the data analysis workflow.\n",
    "  \n",
    "- **Easy Sharing**: The documents can be converted to various formats like HTML, PDF, and slideshows, thereby making it easy to share findings with peers.\n",
    "\n",
    "**Common Uses**\n",
    "\n",
    "Jupyter Notebooks are widely used in data analysis, computational science, artificial intelligence, and academia for:\n",
    "- Data cleaning and transformation\n",
    "- Numerical simulation\n",
    "- Statistical modeling\n",
    "- Machine learning\n",
    "- Much more!\n",
    "\n",
    "**How it Works**\n",
    "\n",
    "Jupyter Notebooks have an interactive user interface with a \"cell\" structure. A notebook document is composed of cells, each of which can contain code, text, images, and more. Cells can be executed independently and in any order, though the sequential execution of cells is common in most workflows.\n",
    "\n",
    "In the following sections, we will explore the user interface, cell types (Markdown & Code), and how to create visual outputs and narratives using Jupyter Notebooks.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2. Understanding Cells in Jupyter Notebooks\n",
    "\n",
    "---\n",
    "\n",
    "#### Markdown Cells\n",
    "\n",
    "**What is Markdown?**\n",
    "\n",
    "Markdown is a lightweight markup language with plain text formatting syntax. It is designed to be easy-to-read and easy-to-write. Markdown cells in Jupyter Notebooks support both Markdown and HTML syntax. Furthermore, you can include mathematical equations using LaTeX syntax.\n",
    "\n",
    "**Basic Markdown Syntax:**\n",
    "- Headers: Use `#` for headers. More `#`s indicate a smaller header.\n",
    "- Text Styles: Use `**` for bold and `_` for italic text.\n",
    "- Lists: Use `-` or `*` for bullet points.\n",
    "- Links: Use `[Description](URL)` to create hyperlinks.\n",
    "- Images: Use `![Alt text](URL)` to embed images.\n",
    "- LaTeX Equations: Use `\\( ... \\)` for inline and `\\[ ... \\]` for block equations.\n",
    "\n",
    "**Example Markdown Cell:**\n",
    "```markdown\n",
    "# This is a Header\n",
    "## This is a Sub-header\n",
    "**Bold Text** and _Italic Text_\n",
    "\n",
    "- Bullet Point 1\n",
    "- Bullet Point 2\n",
    "\n",
    "[Link to Google](https://www.google.com)\n",
    "\n",
    "Inline equation: \\( E = mc^2 \\)\n",
    "Block equation: \n",
    "\\[ E = mc^2 \\]\n",
    "```\n",
    "\n",
    "This is what it looks like when rendered:\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# This is a Header\n",
    "## This is a Sub-header\n",
    "**Bold Text** and _Italic Text_\n",
    "\n",
    "- Bullet Point 1\n",
    "- Bullet Point 2\n",
    "\n",
    "[Link to Google](https://www.google.com)\n",
    "\n",
    "Inline equation: \\( E = mc^2 \\)\n",
    "Block equation: \n",
    "\\[ E = mc^2 \\]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### B. Code Cells\n",
    "\n",
    "**Executing Code:**\n",
    "\n",
    "Code cells within Jupyter Notebooks allow you to write and execute code in a step-by-step manner. When a code cell is executed, its output is displayed below the cell, and any variables, functions, or objects defined will be stored in the notebook's memory for use in subsequent cells.\n",
    "\n",
    "**Supported Languages:**\n",
    "\n",
    "Although Python is the most commonly used language in Jupyter Notebooks, other languages like R and Julia can also be utilized, provided the relevant Jupyter Kernels are installed.\n",
    "\n",
    "**Example Code Cell:**\n",
    "```python\n",
    "# Simple arithmetic operation\n",
    "3 + 4\n",
    "```\n",
    "\n",
    "#### Switching Between Cell Types:\n",
    "\n",
    "- To convert a cell to Markdown: Press `M` (in command mode)\n",
    "- To convert a cell to Code: Press `Y` (in command mode)\n",
    "- To enter command mode from edit mode, press `Esc`. To enter edit mode from command mode, press `Enter`.\n",
    "\n",
    "#### Running Cells:\n",
    "\n",
    "- To run a cell and move to the next one: Press `Shift + Enter`\n",
    "- To run a cell and stay on it: Press `Ctrl + Enter`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "3 + 4"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Variable Persistence and Execution Order in Jupyter Notebooks\n",
    "\n",
    "---\n",
    "\n",
    "#### A. Variables and Code Execution\n",
    "\n",
    "**Variables and Their Scope:**\n",
    "\n",
    "In Jupyter Notebooks, when you create a variable in a code cell and execute it, the variable is stored in the notebook's memory (kernel). This means that once a cell has been run, the variable can be accessed or modified by any other code cell in the notebook, as long as the kernel remains active.\n",
    "\n",
    "**Example:**\n",
    "```python\n",
    "# Code Cell 1\n",
    "my_variable = 10  # Defining a variable\n",
    "```\n",
    "```python\n",
    "# Code Cell 2\n",
    "my_variable += 5  # Accessing and modifying the variable\n",
    "```\n",
    "\n",
    "#### B. Execution Order Matters\n",
    "\n",
    "**Sequential Execution:**\n",
    "\n",
    "One unique aspect of Jupyter Notebooks is the non-linear execution order of cells, meaning you can run cells in any order you like. This is powerful but can sometimes lead to confusion if you're not careful with the order in which you run the cells.\n",
    "\n",
    "**Keeping Track:**\n",
    "\n",
    "The number in the square brackets next to the cell (e.g., `In [3]`) indicates the order in which the cells were run. If there's no number or if there's a `*` symbol (e.g., `In [*]`), the cell has not been run yet or is currently running, respectively.\n",
    "\n",
    "**Example:**\n",
    "```python\n",
    "# Code Cell 3\n",
    "my_variable *= 2  # This will use the modified value from Code Cell 2\n",
    "```\n",
    "\n",
    "#### C. Restarting the Kernel\n",
    "\n",
    "**Clearing Variables:**\n",
    "\n",
    "If you wish to clear all variables and start fresh, you can restart the kernel by clicking on the \"Kernel\" menu and selecting \"Restart\". This will not erase the code or outputs but will erase all variables stored in memory.\n",
    "\n",
    "**Executing All Cells:**\n",
    "\n",
    "To ensure sequential logic in your analysis, you can run all cells in order from the beginning by selecting \"Cell\" > \"Run All\" from the menu after restarting the kernel.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_variable = 10"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "my_result = 2 * my_variable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We will not need to print a variable to see it's content\n",
    "my_result"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. Jupyter Notebooks vs. Stand-Alone Applications in ML/AI Development\n",
    "\n",
    "---\n",
    "\n",
    "#### A. Using Jupyter Notebooks\n",
    "\n",
    "**Exploratory Work:**\n",
    "\n",
    "Jupyter Notebooks are particularly advantageous for exploratory work and data analysis due to their interactive nature. The cell structure allows for step-by-step execution and modification of code, making it easy to iteratively develop and refine models and visualizations.\n",
    "\n",
    "**Advantages:**\n",
    "- **Interactivity:** Immediate feedback on code execution.\n",
    "- **Documentation:** In-line documentation of logic and findings using Markdown.\n",
    "- **Visualization:** Easy visualization of data and results.\n",
    "- **Sharing:** Seamless sharing and presentation of analysis with non-technical stakeholders.\n",
    "\n",
    "**Example Use-Cases:**\n",
    "- Data exploration and visualization\n",
    "- Model prototyping\n",
    "- Academic research and tutorials\n",
    "- Reporting and providing insights on data\n",
    "\n",
    "#### B. Transitioning to Stand-Alone Applications\n",
    "\n",
    "**Production Environments:**\n",
    "\n",
    "When transitioning machine learning models from the development to the production phase, it is common to migrate from Jupyter Notebooks to stand-alone applications. This is because stand-alone applications provide more control over the execution flow and can be more easily integrated into production environments.\n",
    "\n",
    "**Advantages:**\n",
    "- **Scalability:** Better handling of larger systems and architectures.\n",
    "- **Modularity:** Code can be organized into scripts, modules, and packages, enhancing maintainability.\n",
    "- **Testing:** Easier to implement unit testing and continuous integration.\n",
    "- **Automation:** Simplified automation of processes and integration with other services.\n",
    "\n",
    "**Example Use-Cases:**\n",
    "- Deploying machine learning models into production\n",
    "- Developing software applications\n",
    "- Implementing APIs and web services\n",
    "- Automating data pipelines\n",
    "\n",
    "#### C. Best Practices in ML/AI Development\n",
    "\n",
    "**Hybrid Approach:**\n",
    "\n",
    "A hybrid development approach is often adopted in ML/AI projects. Initial data exploration, model development, and validation are performed using Jupyter Notebooks due to their interactive and exploratory nature. Once the model is ready to be deployed or integrated into a larger system, the code is refactored into a stand-alone application.\n",
    "\n",
    "**Key Considerations:**\n",
    "- Use notebooks for interactive development and exploration.\n",
    "- Transition to stand-alone applications for production deployment.\n",
    "- Ensure that code is clean and modular to simplify the transition from development to production.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5. Data Visualization using Matplotlib in Jupyter Notebooks\n",
    "\n",
    "---\n",
    "\n",
    "#### A. Introduction to Data Visualization\n",
    "\n",
    "**Importance:**\n",
    "\n",
    "Data visualization is crucial in understanding the patterns, trends, and insights within data, by converting information into a visual context. This aids in understanding complex data structures and assists in drawing actionable insights, especially in the field of data science and machine learning.\n",
    "\n",
    "#### B. Introducing Matplotlib\n",
    "\n",
    "**Definition:**\n",
    "\n",
    "Matplotlib is a comprehensive library for creating static, interactive, and animated visualizations in Python. It provides a high-level interface for drawing attractive and informative statistical graphics.\n",
    "\n",
    "**Basic Usage:**\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt  # Importing the library"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### C. Creating a Simple Plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjIAAAHHCAYAAACle7JuAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAABN/klEQVR4nO3dd3gUdeLH8fduekISCBBCCqHXUEMVVBCULtWuhHKKHqAop6eCAj8LnseJIrZTaR6IUm2gUgROBQkJLUgLBEiAJLQUEtJ25/cHdzkjLcEks5t8Xs+zz+N+Z2b383WU/bAzO2MxDMNARERExAlZzQ4gIiIicqNUZERERMRpqciIiIiI01KREREREaelIiMiIiJOS0VGREREnJaKjIiIiDgtFRkRERFxWioyIiIi4rRUZESk1G3cuBGLxcLGjRtNef+6desycuTIcn/fkSNHUrdu3XJ/X5HKTEVGpBJ69913sVgsdOrUqUTb2e12Fi5cSKdOnQgICMDX15fGjRszYsQItm7dWkZpzde9e3csFkvhIyAggA4dOjB37lzsdnupvMerr77KqlWrSuW1RCoTV7MDiEj5W7RoEXXr1mXbtm3Ex8fTsGHDYm33+OOP88477zBo0CAeeOABXF1dOXDgAGvWrKF+/fp07twZgFtuuYWLFy/i7u5eltMoV6GhocyYMQOA06dPs3DhQsaMGcPBgwd57bXX/vDrv/rqqwwfPpzBgwf/4dcSqUxUZEQqmYSEBH7++WdWrFjB2LFjWbRoEVOnTr3udikpKbz77rs8/PDD/POf/yyy7M033+T06dOFz61WK56enqWe3Uz+/v48+OCDhc/Hjh1LkyZNmDNnDi+99BJubm4mphOpvHRoSaSSWbRoEdWqVaN///4MHz6cRYsWFWu7hIQEDMOga9euly2zWCwEBgYWPr/SOTLdu3cnIiKC3bt3c+utt+Lt7U3Dhg1ZtmwZAJs2baJTp054eXnRpEkT1q1bV+Q9pk2bhsViYf/+/dx99934+flRvXp1nnjiCXJycq6bPy0tjYkTJxIWFoaHhwcNGzbkb3/72w0fGvL29qZz585kZWUVKXG/l5WVxaRJkwrft0mTJsycORPDMArXsVgsZGVlsWDBgsLDV2ac4yPijFRkRCqZRYsWMXToUNzd3bnvvvs4dOgQ0dHR190uPDwcgKVLl5KdnX1D733+/HkGDBhAp06deP311/Hw8ODee+/ls88+495776Vfv3689tprZGVlMXz4cDIzMy97jbvvvpucnBxmzJhBv379mD17No888sg13zc7O5tbb72Vf/3rX4wYMYLZs2fTtWtXnnvuOZ566qkbmgvAkSNHcHFxoWrVqldcbhgGd955J7NmzaJPnz688cYbNGnShKeffrrI+37yySd4eHhw880388knn/DJJ58wduzYG84lUqkYIlJpbN++3QCMtWvXGoZhGHa73QgNDTWeeOKJYm0/YsQIAzCqVatmDBkyxJg5c6axb9++y9b74YcfDMD44YcfCsduvfVWAzAWL15cOLZ//34DMKxWq7F169bC8e+++84AjHnz5hWOTZ061QCMO++8s8h7/fnPfzYAY9euXYVj4eHhRlRUVOHzl156yfDx8TEOHjxYZNtnn33WcHFxMY4fP37Ned96661G06ZNjdOnTxunT5829u3bZzz++OMGYAwcOLBwvaioKCM8PLzw+apVqwzAePnll4u83vDhww2LxWLEx8cXjvn4+BTJLCLFo29kRCqRRYsWUatWLXr06AFcOqRxzz33sGTJEmw223W3nzdvHnPmzKFevXqsXLmSv/zlLzRr1oyePXty4sSJ625fpUoV7r333sLnTZo0oWrVqjRr1qzIL6j++89Hjhy57DXGjRtX5PmECRMAWL169VXfd+nSpdx8881Uq1aNM2fOFD569eqFzWZj8+bN182+f/9+atasSc2aNWnWrBlvv/02/fv3Z+7cuVfdZvXq1bi4uPD4448XGZ80aRKGYbBmzZrrvq+IXJtO9hWpJGw2G0uWLKFHjx4kJCQUjnfq1Il//OMfrF+/njvuuOOar2G1Whk3bhzjxo3j7Nmz/PTTT7z//vusWbOGe++9l3//+9/X3D40NBSLxVJkzN/fn7CwsMvG4NKhqN9r1KhRkecNGjTAarVy9OjRq77voUOH2L17NzVr1rzi8tTU1GvmhkvXpvnwww+xWCx4enrSqFGjIucFXcmxY8cIDg7G19e3yHizZs0Kl4vIH6MiI1JJbNiwgVOnTrFkyRKWLFly2fJFixZdt8j8VvXq1bnzzju588476d69O5s2beLYsWOF59JciYuLS4nGjd+cEHs1vy9GV2K327n99tt55plnrri8cePG130NHx8fevXqdd31RKR8qciIVBKLFi0iMDCQd95557JlK1asYOXKlbz//vt4eXmV+LXbt2/Ppk2bOHXq1DWLTGk4dOgQ9erVK3weHx+P3W6/5hV1GzRowIULF8q9iISHh7Nu3ToyMzOLfCuzf//+wuX/VZxCJiKX0zkyIpXAxYsXWbFiBQMGDGD48OGXPcaPH09mZiZffvnlVV8jOTmZX3/99bLxvLw81q9fj9VqLfaF9f6I3xext99+G4C+fftedZu7776bLVu28N133122LC0tjYKCgtIN+R/9+vXDZrMxZ86cIuOzZs3CYrEUyezj40NaWlqZ5BCpyPSNjEgl8OWXX5KZmcmdd955xeWdO3emZs2aLFq0iHvuueeK6yQlJdGxY0duu+02evbsSVBQEKmpqXz66afs2rWLiRMnUqNGjbKcBnDpejZ33nknffr0YcuWLfzrX//i/vvvp3Xr1lfd5umnn+bLL79kwIABjBw5ksjISLKystizZw/Lli3j6NGjZZJ94MCB9OjRg8mTJ3P06FFat27N999/zxdffMHEiRNp0KBB4bqRkZGsW7eON954g+DgYOrVq1fiW0iIVEYqMiKVwKJFi/D09OT222+/4nKr1Ur//v1ZtGgRZ8+epXr16pet06RJE958801Wr17Nu+++S0pKCp6enkRERPDhhx8yZsyYsp4GAJ999hkvvvgizz77LK6urowfP56///3v19zG29ubTZs28eqrr7J06VIWLlyIn58fjRs3Zvr06YUnF5c2q9XKl19+yYsvvshnn33GvHnzqFu3Ln//+9+ZNGlSkXXfeOMNHnnkEaZMmcLFixeJiopSkREpBotRnLPpRERMNm3aNKZPn87p06fL5ZsfEXEOOkdGREREnJaKjIiIiDgtFRkRERFxWjpHRkRERJyWvpERERERp6UiIyIiIk6rwl9Hxm63c/LkSXx9fXUJcBERESdhGAaZmZkEBwdjtV79e5cKX2ROnjx52Z11RURExDkkJiYSGhp61eUVvsj890ZtiYmJ+Pn5mZxGREREiiMjI4OwsLAiN1y9kgpfZP57OMnPz09FRkRExMlc77QQnewrIiIiTktFRkRERJyWioyIiIg4LRUZERERcVoqMiIiIuK0VGRERETEaanIiIiIiNNSkRERERGnpSIjIiIiTktFRkRERJyWqUVmxowZdOjQAV9fXwIDAxk8eDAHDhwosk73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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Sample data\n",
    "x = [1, 2, 3, 4, 5]\n",
    "y = [1, 4, 9, 16, 25]\n",
    "\n",
    "# Creating a simple plot\n",
    "plt.plot(x, y)\n",
    "\n",
    "# Adding title and labels\n",
    "plt.title(\"A Simple Plot\")\n",
    "plt.xlabel(\"X-axis\")\n",
    "plt.ylabel(\"Y-axis\")\n",
    "\n",
    "# Displaying the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Explanation:**\n",
    "- **`plt.plot(x, y)`:** Creates a line plot using `x` and `y` data.\n",
    "- **`plt.title()`, `plt.xlabel()`, and `plt.ylabel()`:** Add a title and labels to the axes.\n",
    "- **`plt.show()`:** Displays the plot.\n",
    "\n",
    "#### D. Using Visualization in Analysis\n",
    "\n",
    "**Benefits:**\n",
    "- **Exploration:** Identify patterns and outliers in the data.\n",
    "- **Validation:** Validate model outputs and predictions visually.\n",
    "- **Communication:** Present findings and insights in a comprehensible manner.\n",
    "\n",
    "#### E. Interactive Visualization in Notebooks\n",
    "\n",
    "**In-line Plots:**\n",
    "\n",
    "In Jupyter Notebooks, you can use the `%matplotlib inline` magic command to render the plots directly below the code cells and store them in the notebook document.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### F. Advanced Visualization\n",
    "\n",
    "**Complex Plots:**\n",
    "\n",
    "Matplotlib allows for a wide array of plot types, such as histograms, scatter plots, bar charts, and much more, enabling detailed and multifaceted visual analysis.\n",
    "\n",
    "**Example:**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjIAAAHHCAYAAACle7JuAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy81sbWrAAAACXBIWXMAAA9hAAAPYQGoP6dpAAA280lEQVR4nO3deXhU5f3//9cQkkAgYQ8BEtlBRJYWKkaQRVYJa6CyWAG3YhsoFIWKVkiq34JeVEBFcKlgNRSEBmtBoAEkiIAii6CtFDAiSEBQSCCBMCT374/8Mh9C9jDJzD08H9c1l3Puuc+Z9zsnl3lxlhmHMcYIAADAQpU8XQAAAEBZEWQAAIC1CDIAAMBaBBkAAGAtggwAALAWQQYAAFiLIAMAAKxFkAEAANYiyAAAAGsRZAAfs3XrVjkcDm3dutUj79+kSRNNmDDBI+99s4uNjZXD4fB0GUCFIsgAFezVV1+Vw+FQly5dSrVedna2/va3v6lLly6qXbu2goOD1apVK40bN067du0qp2o9zxN9Z2RkKDY2tsAw+OGHHyo2NrZc3rcwEyZMkMPhcD1CQkLUoUMH/eUvf1FmZqZb3uPVV1/VsmXL3LItoCJV9nQBwM0mPj5eTZo00WeffaYjR46oRYsWJVrvd7/7nRYtWqShQ4fq/vvvV+XKlXXo0CGtX79ezZo105133ilJ6t69uy5duqSAgIDybKPClLRvd8rIyFBcXJwkqWfPnnle+/DDD7Vo0aIKDzOBgYF68803JUnnz5/XP/7xDz3xxBPavXu3VqxYccPbf/XVV1W3bl2OpsE6BBmgAiUnJ2vHjh1KSEjQxIkTFR8fr9mzZxe73unTp/Xqq6/q0Ucf1euvv57ntQULFujMmTOu5UqVKqlKlSpur90TStO3zYwxunz5sqpWrVronMqVK+tXv/qVa/m3v/2tunTpopUrV+rFF19Uw4YNK6JUwOtwagmoQPHx8apVq5aioqI0cuRIxcfHl2i95ORkGWPUtWvXfK85HA6Fhoa6lgu6RqZnz566/fbbdeDAAfXo0UNBQUFq0aKFVq9eLUlKSkpSly5dVLVqVbVu3VqbNm3K8x651158/fXXuu+++xQSEqI6depoypQpunz5crH1nz9/XlOnTlVERIQCAwPVokULPf/888rOznZb37nv8/vf/15NmjRRYGCgwsPDNW7cOJ09e1aSdOXKFc2aNUudOnVSjRo1VK1aNd1999366KOPXNv49ttvVa9ePUlSXFyc63RObGysJkyYoEWLFrneP/eRKzs7WwsWLFDbtm1VpUoV1a9fXxMnTtS5c+fy1NmkSRMNGjRIGzduVOfOnVW1alW99tprxf4cr1WpUiXX0aJvv/220HlXr17Vs88+q+bNmyswMFBNmjTRU089leeUVJMmTfTVV18pKSnJ1dP1R6IAb0WQASpQfHy8oqOjFRAQoDFjxujw4cPavXt3ses1btxYkrRq1SplZGSU6b3PnTunQYMGqUuXLnrhhRcUGBio0aNHa+XKlRo9erQGDhyouXPnKj09XSNHjtSFCxfybeO+++7T5cuXNWfOHA0cOFAvvfSSfv3rXxf5vhkZGerRo4feffddjRs3Ti+99JK6du2qmTNnatq0aW7r++LFi7r77rv18ssvq1+/flq4cKEee+wxff311zpx4oQkKS0tTW+++aZ69uyp559/XrGxsTpz5oz69++v/fv3S5Lq1aunxYsXS5KGDx+ud955R++8846io6M1ceJE9e3bV5Jc4++8846rhokTJ2r69Onq2rWrFi5cqAcffFDx8fHq37+/nE5nnnoPHTqkMWPGqG/fvlq4cKE6duxYZH8FOXr0qCSpTp06hc555JFHNGvWLP385z/X/Pnz1aNHD82ZM0ejR492zVmwYIHCw8N16623unp6+umnS10P4BEGQIX4/PPPjSSTmJhojDEmOzvbhIeHmylTppRo/XHjxhlJplatWmb48OFm3rx55r///W++eR999JGRZD766CPXWI8ePYwks3z5ctfY119/bSSZSpUqmV27drnGN27caCSZpUuXusZmz55tJJkhQ4bkea/f/va3RpL54osvXGONGzc248ePdy0/++yzplq1auZ///tfnnWffPJJ4+fnZ7777ju39D1r1iwjySQkJOR7LTs72xhjzNWrV01mZmae186dO2fq169vHnroIdfYmTNnjCQze/bsfNuKiYkxBf2v8+OPPzaSTHx8fJ7xDRs25Btv3LixkWQ2bNhQZO+5xo8fb6pVq2bOnDljzpw5Y44cOWL+/Oc/G4fDYdq3b++al7ufcu3fv99IMo888kie7T3xxBNGktmyZYtrrG3btqZHjx4lqgfwJhyRASpIfHy86tevr169eknKOTUxatQorVix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VRo3bpymTp2ql19+Wfv27VPLli0l5RyR6dWrl86dO6eaNWuqffv2GjFihGbPnu32vgBUHE4tAfCYt956S0FBQUpOTtaJEyckSY899piqV6/ueuRauXKlunbtqrCwMFWvXl1//OMf9d133+XZ3i9/+UsNHz5cc+fO1bx581whpiC/+93v9Nxzz6lr166aPXu2Dhw4UD5NAihXBBkAHrFjxw7Nnz9fa9eu1R133KGHH35Yxhj96U9/0v79+10PSdq5c6fuv/9+DRw4UGvXrtW+ffv09NNP68qVK3m2mZGRoT179sjPz0+HDx8u8v0feeQRffPNN65TW507d9bLL79cXu0CKCcEGQAVLiMjQxMmTNBvfvMb9erVS3/961/12WefacmSJQoNDVWLFi1cDykn9DRu3FhPP/20OnfurJYtW+rYsWP5tvv444+rUqVKWr9+vV566SVt2bKlyDoiIiL02GOPKSEhQY8//rjeeOONcukXQPkhyACocDNnzpQxRnPnzpUkNWnSRPPmzdOMGTP07bff5pvfsmVLfffdd1qxYoWOHj2ql156SWvWrMkzZ926dXrrrbcUHx+vvn37avr06Ro/frzOnTtXYA1Tp07Vxo0blZycrL179+qjjz5SmzZt3N4rgPLFxb4AKlRSUpJ69+6trVu3qlu3bnle69+/v65evapNmzbJ4XDkeW3GjBl66623lJmZqaioKN15552KjY3V+fPndebMGbVr105TpkzRzJkzJUlOp1ORkZFq3ry5Vq5cme9i38mTJ2v9+vU6ceKEQkJCNGDAAM2fP1916tSpsJ8FgBtHkAEAANbi1BIAALAWQQYAAFiLIAMAAKxFkAEAANYiyAAAAGsRZAAAgLUIMgAAwFoEGQAAYC2CDAAAsBZBBgAAWIsgAwAArEWQAQAA1vr/AAlsic7cGHaFAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(x, y, color='red', marker='o')\n",
    "plt.title(\"A Simple Scatter Plot\")\n",
    "plt.xlabel(\"X-axis\")\n",
    "plt.ylabel(\"Y-axis\")\n",
    "plt.grid(True)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 6. Exporting and Sharing Jupyter Notebooks\n",
    "\n",
    "---\n",
    "\n",
    "#### A. The Versatility of Jupyter Notebooks\n",
    "\n",
    "**Portability:**\n",
    "\n",
    "Jupyter Notebooks can be easily converted and shared in various formats, ensuring that your analysis, code, and findings can be accessed and understood by different audiences, regardless of their technical expertise.\n",
    "\n",
    "#### B. Exporting Notebooks\n",
    "\n",
    "**Various Formats:**\n",
    "\n",
    "Jupyter Notebooks can be exported to numerous formats through the \"File\" > \"Download as\" option in the menu bar. Some of the formats include:\n",
    "- **Notebook (.ipynb):** Preserve the notebook in its interactive format.\n",
    "- **Script (.py):** Extract and save the code cells as a Python script.\n",
    "- **HTML (.html):** Convert the notebook to a static HTML page.\n",
    "- **PDF (.pdf):** Generate a PDF document of the notebook.\n",
    "- **Markdown (.md):** Convert the notebook to a markdown file.\n",
    "\n",
    "#### C. Sharing Notebooks\n",
    "\n",
    "**Different Approaches:**\n",
    "\n",
    "- **GitHub:** Jupyter Notebooks render directly on GitHub, providing an easy way to share your work with peers.\n",
    "  \n",
    "- **Nbviewer:** Share the notebook through Jupyter's nbviewer by providing the GitHub URL.\n",
    "\n",
    "- **Email or Cloud Storage:** Send the .ipynb file directly or share it through cloud storage.\n",
    "\n",
    "- **Binder:** Share interactive, live versions of your notebook by linking your GitHub repository to Binder.\n",
    "\n",
    "#### D. Use-Cases\n",
    "\n",
    "**Adapt to Audience:**\n",
    "\n",
    "- **Non-Technical Audience:** For non-technical stakeholders or broad audiences, consider exporting the notebook as a **PDF** or **HTML** to share your findings while preserving the formatting and visualizations.\n",
    "\n",
    "- **Developers or Data Scientists:** For sharing with other developers or data scientists who might run or modify the code, providing the **.ipynb** file or **.py** script might be more appropriate.\n",
    "\n",
    "- **Web Sharing:** For sharing your insights on web platforms, consider exporting as **Markdown** or **HTML**.\n",
    "\n",
    "#### E. Example: Exporting to HTML\n",
    "\n",
    "**Procedure:**\n",
    "1. Go to \"File\" in the menu bar.\n",
    "2. Hover over \"Download as\".\n",
    "3. Select \"HTML (.html)\" from the dropdown menu.\n",
    "4. The notebook will be converted and downloaded as an HTML file, which can be viewed in any web browser and shared as needed.\n",
    "\n",
    "#### F. Keeping Notebooks Clean\n",
    "\n",
    "**Before Exporting:**\n",
    "- Ensure that the code cells have been executed in order and outputs are visible.\n",
    "- Add sufficient comments and markdown explanations to ensure clarity.\n",
    "- Check for any unnecessary or error cells and remove or fix them."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}