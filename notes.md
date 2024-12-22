# Notes About This Repository Index

My Github repositories is updated periodically as I gather together some of the work that I've been doing. 

I tend to use Github as a sort of first entry notepad for working on ideas for technical projects. 

The methodology I use to actually assemble this repository index periodically is two-fold and (of course) uses LLMs!

- Firstly, I use a Python script to generate an organized CSV of my repositories. 
- Then I provide that to a large language model with a generous context length limit and support for long outputs if possible. 

As I only get around to updating this index every few months or so, I tend to just rewrite a new prompt every time. But generally, they follow a structure that's very similar to this, instructing the model to group my repositories into different categories and apply some formatting. 

With a little bit of effort in fixing up formatting and cobbling together outputs. I get something reasonably close to a well organized list of my current repositories.  

Here's one of the prompts I have used:

> The attached CSV contains a list of my public GitHub repositories. Your task is to organize this list into a markdown file that can serve as an index to it. You should gather together groups of repositories reflecting common interests or common topics. The index should be ordered like this, alphabetically according to the group name. The group name should be a H1. Then, under that group name, there should be individual repositories within that group. Those should also be ordered alphabetically. The presentation for the repository should be that the repository name is a H2. Then the description. And then a shields.io markdown badge. The shields.io markdown badge should contain a link to the repository. And it should just have the repository name as the display text. You can and should also convert the titles into more readable versions. For example, I have a repository whose title is awesome-chatGPT-prompts. This can be reformatted in the header as Awesome ChatGPT Prompts. You can infer the intended display from the name. Output the whole index in one go if you can. Each repository should belong to at least one group. If you need to use a chunking strategy to provide the output, do so and with each successive chunk resume from where you left off previously. "