---
title:  "Why Reinforcement Learning (RL) is hot again?"
date:   2025-04-15
description: "Reinforcement Learning (RL)"
categories:
  - "AI Engineering"
  - "LLM"
tags:
  - "AI Engineering"
  - "LLM"
comments: true
authors:
   - dannyzheng
---

Just finished an incredible interview with Wu Yi — a Tsinghua alum and former OpenAI researcher — and his take on Reinforcement Learning (RL) was one of the clearest I’ve seen!

### 🔍 1. What is RL really about?
Wu Yi explains that RL is very different from traditional supervised learning (like image classification). In supervised learning, we train models using a fixed set of labeled data — one-shot answers.

RL, on the other hand, is more like playing a game: you need to make a sequence of decisions (serve, move, react), and there's no single “correct” path. The quality of your decisions is judged by the final outcome (win or lose). It’s about multi-step decision-making — much closer to how the real world works.

### 🤖 2. Why is RL hot again? What’s its connection to LLMs?
LLMs like GPT-3 were initially great at reciting facts but not great at following instructions.

OpenAI used RL to fix that — specifically Reinforcement Learning from Human Feedback (RLHF). Humans rated model responses, which trained a “reward model” to guide LLMs to be more helpful, honest, and harmless.

Important insight: RLHF made LLMs more aligned, but not necessarily more intelligent.

### 🧠 3. Can RL make LLMs smarter?
People realized that humans solve complex problems by thinking first — step by step. So, what if LLMs could simulate “slow thinking” too?

Turns out, if you let the model “generate more thoughts” (i.e., more tokens as intermediate reasoning steps), it mimics thought processes. And again, RL is used to train this — because we only care about the final answer being correct, not how it reasoned in between. Classic RL logic.

### 💡 4. RL + LLM = Power Combo
Can RL work alone? Not really. RL is great at decision-making, but weak at understanding. That’s where LLMs come in — strong at comprehension and memory.

So the winning formula is: LLM (understanding/memory) + RL (reasoning/decision-making) = stronger AI
This is how OpenAI is building agents like Operator and Deep Research.

### 🚀 5. Future of RL & its challenges
RL still has massive untapped potential — its scaling laws are just getting started.

Different companies are taking different paths:

OpenAI is building agents

Anthropic is focusing on code

DeepSeek is pushing general reasoning (even answering philosophical questions)

But RL is hard: high barrier to entry, complex infra, data requirements, and a “black magic” vibe. Top talent is rare.

### 🌱 6. Life Lessons from RL (this part was brilliant!)
Classic RL seeks one “optimal policy” and sticks with it. But Wu Yi found that humans are diversity-driven — we naturally try different paths to win.

His life advice? Maximize entropy: try different things, especially while you’re young and the cost of failure is low.

**Life is like RL — you have to explore to find your own “reward function” (goals, meaning).**

> Source: https://www.xiaoyuzhoufm.com/episode/67efcaf5f9578163d601286a