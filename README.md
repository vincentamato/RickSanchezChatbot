
# Rick Sanchez Chatbot

![alt text](https://www.rollingstone.com/wp-content/uploads/2022/08/22-RAM-S6-KEY-ART-1080x1080-1-e1661990077221.png?w=831&h=554&crop=1)

## Project Overview
This project involves fine-tuning the Llama-2-chat model using Prompt Engineering and Fine-Tuning (PEFT) to create a chatbot that impersonates Rick Sanchez from the animated series "Rick and Morty." The model is trained to mimic Rick's unique style of dialogue and wit, using scripts from seasons 1-3 of the show.

## Installation

### Prerequisites
- Python 3.8 or above
- CUDA-compatible GPU (Recommended for training)

### Steps
1. Clone the repository:
   ```
   git clone [repository URL]
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Training the Model
Run the Jupyter Notebook `RickSanchez-7b-q.ipynb` to start the fine-tuning process. Keep in mind you will need access to the Llama-2-chat model, which can be obtained [here](https://ai.meta.com/resources/models-and-libraries/llama-downloads/).

### Chatting with Rick
Run `test.py` to interact with the chatbot and experience a conversation with Rick Sanchez.

## Dataset
The dataset comprises scripts from seasons 1-3 of "Rick and Morty," focusing on dialogues involving Rick Sanchez. These scripts are formatted and processed to be suitable for fine-tuning the language model.

## Model
The base model is Llama-2-chat, a variant of the Llama model designed for chat applications. PEFT is used to adapt this model to accurately reflect Rick Sanchez's speech style in the generated responses.

## Acknowledgments
- "Rick and Morty" creators and scriptwriters.
- [andradaolteanu](https://www.kaggle.com/andradaolteanu) for the dataset.
- The developers of the Llama-2-chat model.
