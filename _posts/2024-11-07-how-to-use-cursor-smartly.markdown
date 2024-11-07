---
layout: post
title:  "Cursor AI Done Right: Lessons from Building Multiple MVPs"
date:   2024-11-07 06:22:53 -0700
categories: [AI]
---

> Cursor is really dumb if not given enough context about your project.
> Here what you can do to improve your Cursor workflow

## 1. Brainstorm first, code second

Claude/o1 are your best friends here. You should create a whole document containing every single detail of your project.

- core features 
- goals & objectives
- tech stack & packages
- project folder structure
- database design
- landing page components 
- color palette 
- copywriting 

All this should be put into an `instruction.md` (name it however you want) so Cursor can index at any time.

## 2. Get a `.cursorrules` file 

Many ignore this step. I get it’s daunting to write a `.cursorrules` file but it will help tremendously.

This is a great repo I always recommend to get you started. Choose your stack and edit it to match your preferences: [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)


## 3. Use v0 for landing page 

- Get your core features, color palette and components from your `instruction.md` file you got. 

- Bonus tip is to use screenshots as reference from other landing pages just so v0 gets your idea. 

- Use component libraries I recommend shadcn since v0 works great with it. I also use MagicUI. 

Remember, you don’t have to get it perfect with v0. 
You only need something good enough you can take and edit later in cursor.

## 4. Chat vs Composer

- Use chat for smaller tasks and for explaining code/commands. Use it to ask questions and navigate your project. 

- Use composer for writing the code, tag your `instruction.md` inside the composer always and tell him to update it as the project progresses.

- Only ask composer to do one task at a time. Make it make the changes step by step, if you ask to it to edit multiple files it will hallucinate and you will lose control.

- Always verify the code is clean before approving the change. 

- Save your claude credits for the composer and use gpt-4o-mini with chat.

## 5. Tag your docs

- Copy the documentation for the framework you use.

- Go to Cursor Settings > Features > Docs 

- Paste the links and use them inside chat/composer with `@Docs`
