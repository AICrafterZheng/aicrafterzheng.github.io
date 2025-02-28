---
title: "What is RAG?"
date:   2024-12-07 
description: "What is RAG?"
categories:
  - "AI Engineering"
  - "Retrieval-Augmented Generation"
tags:
  - "AI Engineering"
date: 2024-10-15
comments: true
authors:
   - dannyzheng
---
## Introduction🚀
RAG is a popular method that improves accuracy and relevance by finding the right information from reliable sources and transforming it into useful answers. 

Large Language Models are trained on a fixed dataset, which limits their ability to handle private or recent information. They can sometimes "hallucinate", providing incorrect yet believable answers. Fine-tuning can help but it is expensive and not ideal for retraining again and again on new data. The Retrieval-Augmented Generation (RAG) framework addresses this issue by using external documents to improve the LLM's responses through in-context learning. RAG ensures that the information provided by the LLM is not only contextually relevant but also accurate and up-to-date.

![final diagram](https://github.com/user-attachments/assets/508b3a87-ac46-4bf7-b849-145c5465a6c0)

There are four main components in RAG:
<!-- more -->
**Indexing:** First, documents (in any format) are split into chunks, and embeddings for these chunks are created. These embeddings are then added to a vector store.

**Retriever:** Then, the retriever finds the most relevant documents based on the user's query, using techniques like vector similarity from the vector store.

**Augment:** After that, the Augment part combines the user's query with the retrieved context into a prompt, ensuring the LLM has the information needed to generate accurate responses.

**Generate:** Finally, the combined query and prompt are passed to the model, which then generates the final response to the user's query.

These components of RAG allow the model to access up-to-date, accurate information and generate responses based on external knowledge. However, to ensure RAG systems are functioning effectively, it’s essential to evaluate their performance.

## RAG Evaluation📊
Evaluating RAG applications is important for understanding how well these systems work. We can see how effectively they combine information retrieval with generative models by checking their accuracy and relevance. This evaluation helps improve RAG applications in tasks like text summarization, chatbots, and question-answering. It also identifies areas for improvement, ensuring that these systems provide trustworthy responses as information changes.

![evals diagram](https://github.com/user-attachments/assets/65c2b5af-a931-40c5-b006-87567aef019f)



## RAG Techniques⚙️

| Technique                    | Tools                        | Description                                                       | Notebooks |
|---------------------------------|------------------------------|--------------------------------------------------------------|-----------|
| Naive RAG      | LangChain, Pinecone, Athina AI                    | Combines retrieved data with LLMs for simple and effective responses.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/naive_rag.ipynb) |
| Hybrid RAG      | LangChain, Chromadb, Athina AI                    | Combines vector search and traditional methods like BM25 for better information retrieval.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/hybrid_rag.ipynb) |
| Hyde RAG      | LangChain, Weaviate, Athina AI                    | Creates hypothetical document embeddings to find relevant information for a query.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/hyde_rag.ipynb) |
| Parent Document Retriever      | LangChain, Chromadb, Athina AI                    | Breaks large documents into small parts and retrieves the full document if a part matches the query.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/parent_document_retriever.ipynb) |
| RAG fusion      | LangChain, LangSmith, Qdrant, Athina AI                    | Generates sub-queries, ranks documents with Reciprocal Rank Fusion, and uses top results for accurate responses.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/fusion_rag.ipynb) |
| Contextual RAG      | LangChain, Chromadb, Athina AI                    | Compresses retrieved documents to keep only relevant details for concise and accurate responses.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/contextual_rag.ipynb) |
| Rewrite Retrieve Read     | LangChain, Chromadb, Athina AI                    | Improves query, retrieves better data, and generates accurate answers.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/rewrite_retrieve_read.ipynb) |
| Corrective RAG      | LangChain, LangGraph, Chromadb, Athina AI                    | Refines relevant documents, removes irrelevant ones or does the web search.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/corrective_rag.ipynb) |
| Self RAG     | LangChain, LangGraph, FAISS, Athina AI                    | Reflects on retrieved data to ensure accurate and complete responses.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/self_rag.ipynb) |
| Adaptive RAG      | LangChain, LangGraph, FAISS, Athina AI                    | Adjusts retrieval methods based on query type, using indexed data or web search.| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/athina-ai/rag-cookbooks/blob/main/adaptive_rag.ipynb) |