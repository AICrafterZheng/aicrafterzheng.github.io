---
layout: post
title:  "Top best practices for building production-ready AI apps"
date:   2024-11-04 06:22:53 -0700
categories: [AI]
---


1. **Build evals** 
- Define test cases to ensure you're actively improving your app & not causing any regressions.

2. **Break down one LLM call into multiple** 
- AI systems do a lot better when you have many LLM calls chained together. i.e, instead of sending an LLM call to a model to generate code, send it to a "architect" model to generate a plan, then a "coding" model to generate code, then a "reviewer" model to verify.

3. **Start simple** (with 1 LLM call)
- Then iterate with prompt engineering (few shot examples, chain of thought, descriptive prompts) before building a more complex system with chained LLM calls.

4. **Use RAG** 
- When dealing with data you need the LLM to use as context, use RAG(then iterate with your evals to try different chunking/embedding strategies, adding a re-ranker, ect..).

5. **Use finetuning**
- When you want to have the LLM optimize on a domain-specific thing or on a specific style (i.e, write emails like you do), use finetuning.

6. **When launching, ship with observability and look at the data.** 
- It's so important to look at how people are using your system, then you can do things like segment customer prompts, run evals on them, and get great info on where you need to improve your AI system.

(source: [@nutlope](https://x.com/nutlope/status/1852359455884583283))
