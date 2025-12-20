# Week 2: Prompts, Chains & Memory in LangChain

## 📚 Overview

This week focuses on three **core building blocks** of LangChain that enable you to build production-ready AI applications:

1. **Prompts** - How to structure and template instructions for LLMs
2. **Chains** - How to connect multiple operations together
3. **Memory** - How to maintain conversation context and build stateful chatbots

## 🎯 Learning Objectives

By the end of this module, you will be able to:

- ✅ Create reusable prompt templates
- ✅ Build chains that connect prompts with LLMs
- ✅ Implement conversation memory for context-aware chatbots
- ✅ Test and debug multi-turn conversations
- ✅ Write production-ready chatbot code

## 📁 What's in This Folder?

```
Week 2 Working with Prompts, Chains & Memory/
├── week2-Prompts, chains, Memory - LangChain.ipynb    # Main notebook with 6 sections
├── requirements.txt                                     # All Python dependencies
└── README.md                                            # This file
```

## 🚀 Quick Start

### 1. Installation

Install all required packages:

```bash
pip install -r requirements.txt
```

**Or manually:**
```bash
pip install langchain-core langchain-openai langchain-community openai python-dotenv
```

### 2. Environment Setup

Create a `.env` file in this folder:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Get your API key: https://platform.openai.com/api-keys

### 3. Run the Notebook

Open the notebook in Jupyter/VS Code:

```bash
jupyter notebook "week2-Prompts, chains, Memory - LangChain.ipynb"
```

Or open directly in VS Code.

## 📖 Notebook Structure

The notebook is divided into **6 comprehensive sections**:

### Section 1: Basic Prompt Template
- **What:** Creating structured prompts with placeholders
- **Why:** Reusable, maintainable prompt engineering
- **Time:** 5 minutes
- **Outcome:** Understand `PromptTemplate.from_template()`

### Section 2: Building Chains - Translate + Summarize
- **What:** Connecting multiple prompts and LLM calls using the `|` operator
- **Why:** Build complex workflows (not just Q&A)
- **Time:** 10 minutes
- **Outcome:** Master chain composition and pipeline building

### Section 3: Adding Conversation Memory
- **What:** Making chatbots that remember conversation history
- **Why:** Create natural, context-aware conversations
- **Time:** 10 minutes
- **Outcome:** Understand `RunnableWithMessageHistory` and `ChatMessageHistory`

### Section 4: Interactive Chatbot Template
- **What:** Complete code template for building your own chatbot
- **Why:** Starting point for mini-projects
- **Time:** 5 minutes
- **Outcome:** Ready-to-use template for chatbot development

### Section 5: Testing & Verification Guide
- **What:** 5 categories of test cases for validating chatbots
- **Why:** Ensure memory works correctly
- **Time:** Variable (run tests yourself)
- **Outcome:** Confidence that your chatbot works as expected

### Section 6: Production-Ready Implementation
- **What:** Best practices code demonstrating real-world patterns
- **Why:** Learn how to write professional chatbot code
- **Time:** 10 minutes
- **Outcome:** Understanding of system messages, configuration, and error handling

## 💡 Key Concepts

### Prompts
```python
from langchain_core.prompts import PromptTemplate

template = "Summarize: {content}"
prompt = PromptTemplate.from_template(template)
output = prompt.format(content="Some text")
```

### Chains
```python
# Chain operations together with |
chain = prompt | llm | another_prompt | llm
result = chain.invoke({"input": "data"})
```

### Memory
```python
# Add memory to conversations
chatbot = RunnableWithMessageHistory(
    prompt | llm,
    get_history,
    input_messages_key="input",
    history_messages_key="history"
)
```

## 🧪 Testing Your Chatbot

The notebook includes comprehensive testing guides:

### Memory Tests
Verify the chatbot remembers user information:
- User introduces name → Bot recalls name later
- User shares preferences → Bot recalls preferences
- Multi-turn conversation flow

### Interaction Tests
Verify natural conversation:
- Follow-up questions based on context
- Fun/creative questions
- Learning-focused questions

### Edge Cases
- Empty inputs
- Very long conversations
- Session switching

## ⚠️ Common Issues & Solutions

### Issue: "OPENAI_API_KEY not found"
**Solution:** 
1. Create `.env` file in this folder
2. Add your API key: `OPENAI_API_KEY=sk-...`
3. Run `load_dotenv()` before using OpenAI

### Issue: "Memory doesn't work, bot doesn't recall info"
**Solution:**
1. Check you're using same `session_id` across turns
2. Verify `ChatMessageHistory()` is being stored
3. Ensure `config={"configurable": {"session_id": "..."}}` is passed to `invoke()`

### Issue: "ModuleNotFoundError: No module named 'langchain_openai'"
**Solution:**
```bash
pip install --upgrade langchain-openai
```

### Issue: "Bot gives generic answers"
**Solution:** Add a system prompt to guide behavior:
```python
("system", "You are a helpful assistant. Remember what the user tells you...")
```

## 📚 Code Patterns to Remember

### Pattern 1: Simple Prompt
```python
prompt = PromptTemplate.from_template("Summarize: {text}")
```

### Pattern 2: Chain Two Operations
```python
chain = prompt1 | llm | prompt2 | llm
```

### Pattern 3: Conversation with Memory
```python
chatbot = RunnableWithMessageHistory(
    prompt | llm,
    lambda config: store[config["session_id"]],
    input_messages_key="input",
    history_messages_key="history"
)
```

## 🎓 Mini Projects

After completing this week, try building:

1. **Language Translator Chatbot**
   - Remember language preferences
   - Translate between languages
   - Store translation history

2. **Code Explanation Bot**
   - Remember code snippets user shares
   - Explain code with context
   - Answer follow-up questions about the code

3. **Learning Buddy**
   - Remember user's learning goals
   - Generate practice questions
   - Track topics covered

4. **Customer Support Chatbot**
   - Remember customer information
   - Handle multi-turn issues
   - Reference previous conversations

## 📖 Additional Resources

### LangChain Documentation
- Prompts: https://python.langchain.com/docs/modules/model_io/prompts/
- Chains: https://python.langchain.com/docs/modules/chains/
- Memory: https://python.langchain.com/docs/modules/memory/

### OpenAI API
- Documentation: https://platform.openai.com/docs
- Models: https://platform.openai.com/docs/models
- API Keys: https://platform.openai.com/api-keys

### Best Practices
- Prompt Engineering Guide: https://platform.openai.com/docs/guides/prompt-engineering
- LangChain Best Practices: https://python.langchain.com/docs/guides/

## 🔄 Learning Path

```
Week 1: Introduction to LangChain
    ↓
Week 2: Prompts, Chains & Memory ← YOU ARE HERE
    ↓
Week 3: AI Resume Analyzer
    ↓
Week 4: RAG Projects
    ↓
... continue building more complex applications
```

## 💬 Questions & Troubleshooting

If you encounter issues:

1. **Check the notebook's Section 5** - It has a debugging table with common problems
2. **Verify your .env file** - Make sure API key is set correctly
3. **Test each section independently** - Run sections one by one to find issues
4. **Review the code comments** - Every step has detailed explanations

## 📝 Practice Exercises

### Exercise 1: Modify the Translation Prompt
Change the translation target language (Spanish, Hindi, etc.)

### Exercise 2: Create a New Chain
Build a chain: English → French → Spanish translation pipeline

### Exercise 3: Add System Prompt
Add a system message to the chatbot (e.g., "You are a pirate..."). Notice behavior change.

### Exercise 4: Test Memory Limits
How long can the conversation be before memory issues occur?

### Exercise 5: Multi-Session Chatbot
Create multiple sessions with different users in one notebook

## ✅ Checklist: Before Moving to Week 3

- [ ] Installed all packages from `requirements.txt`
- [ ] Created `.env` file with OpenAI API key
- [ ] Ran all 6 sections in the notebook
- [ ] Memory tests passed (bot recalled information correctly)
- [ ] Built a simple chatbot and tested it
- [ ] Completed at least 2 practice exercises
- [ ] Understand prompts, chains, and memory concepts

## 🎉 Next Steps

Once you complete this week:

1. **Review the code** - Make sure you understand each line
2. **Experiment** - Try modifying prompts, adding features
3. **Build something** - Create your own mini chatbot
4. **Move to Week 3** - AI Resume Analyzer project

## 👨‍🏫 For Instructors

This notebook is designed for:
- **Duration:** 1-2 hours of instruction + practice
- **Difficulty:** Intermediate (assumes Week 1 knowledge)
- **Group Size:** Individual or small groups
- **Prerequisites:** Python basics, Week 1 completion

The notebook includes:
- ✅ Step-by-step code with detailed comments
- ✅ Concept explanations before code
- ✅ Working examples for each concept
- ✅ Testing and verification guide
- ✅ Production-ready code patterns
- ✅ Comprehensive summary and next steps

---

**Last Updated:** December 20, 2025  
**Version:** 1.0  
**Author:** Learn with Sarvesh - 12-Week LangChain Cohort