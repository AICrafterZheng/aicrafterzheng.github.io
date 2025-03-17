# Pretraining 
training a neural network meaning just discover a set of parameters that seems to be consistent with statistics of the training data.

1. When you talk to ChatGPT, you are talking to labeling engineers.

## Hallucinations:
Mitigation #1:

Use model interrogation to discover model's knowledge, and programmatically augment its training dataset with knowledge-based refusals in cases where the model doesn't know.

Mitigation #2:
Allow the model to search.

Vague recollection vs working memory:
Knowledge in the parameters == Vague recollection (e.g. of something you read 1 month ago)
Knowledge in the tokens of the context window == Working memory 

## Knowledge self:
The LLM has no knowledge of self "out of the box"
If you do nothing, it will probably think it is ChatGPT, developed by OpenAl.
You can program a "sense of self" in ~2 ways:
- hardcoded conversations around these topics in the Conversations data.
- "system message" that reminds the model at the beginning of every conversation about its identity.

## Models need tokens to think:

## Models can't count

## Models are not good with spelling.


## Resources:
https://tiktokenizer.vercel.app/?model=cl100k_base
https://bbycroft.net/llm

Old model:
https://huggingface.co/playground?modelId=tiiuae/falcon-7b-instruct

The Llama 3 Herd of Models:
https://arxiv.org/abs/2407.21783





