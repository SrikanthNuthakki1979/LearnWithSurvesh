# 🚀 Week 1: Introduction to LangChain & AI Workflows

Welcome to Week 1 of the 12-Week LangChain Cohort! This week lays the foundation for building powerful AI applications using LangChain and OpenAI.

---

## 📚 Learning Objectives

By the end of this week, you will be able to:

- ✅ **Understand LangChain fundamentals** and its role in AI development
- ✅ **Set up a complete LangChain development environment**
- ✅ **Work with Large Language Models (LLMs)** through LangChain wrappers
- ✅ **Create dynamic Prompt Templates** for consistent AI interactions
- ✅ **Build Chains** to connect multiple AI operations
- ✅ **Develop custom Tools** to extend AI capabilities
- ✅ **Understand AI Agents** and autonomous decision-making

---

## 🎯 Topics Covered

### 1️⃣ **LLMs (Large Language Models)**
- Introduction to ChatOpenAI and OpenAI wrappers
- Understanding model parameters (temperature, model selection)
- Response handling and text extraction
- Error handling and retry logic
- Comparing different models (GPT-3.5-turbo vs GPT-4o-mini)

### 2️⃣ **Prompts — Giving Context to LLMs**
- Creating reusable PromptTemplates
- Working with single and multiple variables
- Implementing few-shot learning
- Input validation and error handling
- Best practices for prompt engineering

### 3️⃣ **Chains — Combining Logic Steps**
- Understanding RunnableSequence and the pipe operator (`|`)
- Building single-step chains
- Creating multi-step workflows
- Combining different models in chains
- Migration from old LLMChain to modern patterns

### 4️⃣ **Tools — Extending Model Capabilities**
- Creating custom tools with the `Tool` class
- Modern `@tool` decorator approach
- Input validation in tools
- Building test harnesses
- Real-world tool applications

### 5️⃣ **Agents — The Brains with Autonomy**
- Understanding AI workflow architecture
- Building multi-step pipelines
- Combining translation and summarization
- Introduction to autonomous agents

---

## 🛠️ Prerequisites

### Required Software
- **Python**: Version 3.8 or higher
- **pip**: Python package manager
- **Text Editor/IDE**: VS Code (recommended), PyCharm, or Jupyter Notebook
- **Git**: For version control (optional but recommended)

### Required Accounts
- **OpenAI Account**: Sign up at [platform.openai.com](https://platform.openai.com)
- **API Key**: Generate from OpenAI dashboard (requires payment method)

---

## 📦 Installation & Setup

### Step 1: Install Required Packages

**Option A: With Version Numbers (Recommended for Production)**
```bash
pip install langchain==1.0.5 openai==2.6.0 python-dotenv==1.2.1 langchain-openai==0.1.0 langchain-community==0.0.29
```

**Option B: Latest Versions (Easier for Learning)**
```bash
pip install langchain openai python-dotenv langchain_openai langchain_community
```

### Step 2: Set Up Environment Variables

1. Create a `.env` file in your project directory:
```bash
touch .env  # On Mac/Linux
# OR
New-Item .env  # On Windows PowerShell
```

2. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```

3. **Important**: Add `.env` to your `.gitignore` file to prevent committing sensitive data:
```bash
echo ".env" >> .gitignore
```

### Step 3: Verify Installation

Check installed package versions:
```bash
pip show langchain openai python-dotenv langchain-openai langchain-community
```

---

## 📁 Files in This Week's Folder

- **`Week1-lws_Student+HW.ipynb`**: Main notebook with all lessons and homework solutions
- **`Week1-lws-Student.ipynb`**: Clean version without homework (if available)
- **`README.md`**: This file - your guide to Week 1
- **`.env`**: Your API keys (create this file yourself, do NOT commit)

---

## 📝 Homework Assignments

### **Section 1: LLMs (5 Questions)**

#### Q1: Text Extraction Methods
- Extract text from LLM responses
- Show at least two methods
- Explain your preferred approach

#### Q2: Temperature Experimentation
- Test temperature values: 0.0, 0.7, 1.0
- Record outputs for each
- Create comparison table

#### Q3: Error Handling
- Implement try-except with retry logic
- Handle missing API keys and network errors
- Explain robustness improvements

#### Q4: Model Comparison
- Compare GPT-3.5-turbo and GPT-4o-mini
- Provide recommendation for one-line definitions
- Justify your choice

#### Q5: Temperature Testing
- Test with temperatures: 0.3, 0.6, 0.9
- Select your favorite output
- Explain your preference

---

### **Section 2: Prompts (5 Questions)**

#### Q1: Summarization Template
- Create template for paragraph summarization
- Use `PromptTemplate.from_template()`
- Format with sample paragraph

#### Q2: Multi-Variable Template
- Build template with `{topic}` and `{tone}`
- Format with: topic="prompt engineering", tone="simple"
- Show formatted output

#### Q3: Missing Variable Handling
- Demonstrate error when variable is missing
- Explain why error occurs
- Show how to avoid it

#### Q4: Few-Shot Learning
- Create template with 2+ examples
- Add placeholder for new input
- Format and display result

#### Q5: Input Validation
- Implement validation function
- Check for empty and overly long inputs
- Show valid and invalid examples

---

### **Section 3: Chains (3 Questions)**

#### Q1: Basic Chain Execution
- Run provided chain example
- Extract and print text only
- Show both full output and clean text

#### Q2: Summarization Chain
- Modify prompt from translation to summarization
- Create and run new chain
- Display results

#### Q3: Multi-Model Chain
- Use GPT-3.5-turbo for translation
- Use GPT-4o-mini for polishing
- Compare outputs and state preference

---

### **Section 4: Tools (3 Questions)**

#### Q1: Enhanced Weather Function
- Add temperature and condition details
- Return formatted information
- Show example outputs

#### Q2: Input Validation
- Validate city name is not empty
- Return helpful error message
- Demonstrate with valid and empty inputs

#### Q3: Test Harness
- Create automated test for multiple cities
- Collect results in a list
- Display formatted output

---

## 🎓 Mini Projects

### **AI Idea Generator**
Build a creative startup idea generator:
- Uses high temperature (0.8) for creativity
- Takes topic as input
- Generates 3 startup ideas
- Interactive user input

**Try these topics:**
- AI in healthcare
- Fintech
- Education technology
- Sustainability
- Mental health

---

## 🏆 Assignment Submission

### Required Deliverables:
1. **Completed notebook** with all homework solutions
2. **"Hello LangChain" script** that explains topics in 3 points
3. **Screenshot of outputs** from your runs
4. **Share in community** or class repository

### Submission Format:
```python
# Include your name and date
# Name: [Your Name]
# Date: [Submission Date]
# Week: 1 - Introduction to LangChain

# Your code here...
```

---

## 🔑 Key Concepts Summary

### **Temperature Parameter**
- **0.0**: Deterministic, factual, consistent
- **0.7**: Balanced creativity
- **1.0+**: Creative, diverse, unpredictable

### **Prompt Templates Benefits**
- Reusability across different inputs
- Consistency in prompt structure
- Easy maintenance and updates
- Type safety and validation

### **Chain Components**
- **Prompt**: Formats input
- **LLM**: Processes request
- **Pipe (`|`)**: Connects components
- **Invoke**: Executes the chain

### **Tool Purposes**
- Access real-time data
- Perform calculations
- Interact with external systems
- Extend LLM capabilities

---

## 📖 Additional Resources

### Official Documentation
- [LangChain Docs](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)

### Learning Materials
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [LangChain Cookbook](https://github.com/langchain-ai/langchain/tree/master/cookbook)
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook)

### Community
- [LangChain Discord](https://discord.gg/langchain)
- [LangChain Twitter](https://twitter.com/LangChainAI)
- Class discussion forum/Slack channel

---

## ⚠️ Common Issues & Solutions

### Issue 1: API Key Not Found
**Error**: `openai.error.AuthenticationError: No API key provided`

**Solution**:
1. Check `.env` file exists in project directory
2. Verify `OPENAI_API_KEY=your-key` is correctly formatted
3. Ensure `load_dotenv()` is called before using API
4. Restart Python kernel/notebook

### Issue 2: Module Not Found
**Error**: `ModuleNotFoundError: No module named 'langchain_openai'`

**Solution**:
```bash
pip install langchain-openai
```

### Issue 3: Rate Limit Errors
**Error**: `RateLimitError: Rate limit exceeded`

**Solution**:
- Wait a few seconds between requests
- Implement retry logic with exponential backoff
- Check your OpenAI usage limits
- Upgrade your OpenAI plan if needed

### Issue 4: Temperature Warnings
**Warning**: Temperature values outside typical range

**Solution**:
- Use 0.0-2.0 for OpenAI models
- Most use cases: 0.0-1.0
- Higher values = more randomness

---

## 🎯 Success Criteria

You've successfully completed Week 1 when you can:

- [ ] Set up LangChain environment without errors
- [ ] Create and invoke LLMs with different parameters
- [ ] Build reusable prompt templates
- [ ] Chain multiple operations together
- [ ] Create and test custom tools
- [ ] Complete all homework assignments
- [ ] Run the mini project successfully
- [ ] Understand the AI workflow architecture

---

## 📅 Next Week Preview

**Week 2: Working with Prompts, Chains & Memory**
- Advanced prompt engineering techniques
- Conversation memory management
- Complex chain patterns
- State management in AI applications

---

## 💬 Getting Help

### If You're Stuck:
1. **Review the notebook** - All solutions are documented with explanations
2. **Check error messages** - Read them carefully for clues
3. **Search documentation** - Links provided in Resources section
4. **Ask in community** - Fellow students and instructors are here to help
5. **Debug systematically** - Test one component at a time

### Questions to Ask:
- What error message am I seeing?
- What was I trying to accomplish?
- What have I already tried?
- Can I share a code snippet?

---

## 🌟 Tips for Success

1. **Type the code yourself** - Don't just copy-paste, understand each line
2. **Experiment freely** - Try different parameters and prompts
3. **Read error messages** - They often tell you exactly what's wrong
4. **Start simple** - Get basics working before adding complexity
5. **Take notes** - Document your learnings and discoveries
6. **Practice daily** - Even 30 minutes a day builds strong skills
7. **Share your work** - Teaching others reinforces your learning

---

## 📊 Time Estimates

- **Setup & Installation**: 30-45 minutes
- **Section 1 (LLMs)**: 1-2 hours
- **Section 2 (Prompts)**: 1-2 hours
- **Section 3 (Chains)**: 1-1.5 hours
- **Section 4 (Tools)**: 1-1.5 hours
- **Section 5 (Agents)**: 30-45 minutes
- **Mini Project**: 30 minutes
- **Total Estimated Time**: 6-9 hours

*Pace yourself and take breaks! Learning should be enjoyable.*

---

## 🎉 Congratulations!

You're taking the first step in mastering LangChain and building powerful AI applications. Week 1 provides the essential foundation for everything you'll build in the coming weeks.

**Remember**: Every expert was once a beginner. Stay curious, keep coding, and don't hesitate to ask for help!

---

**Happy Learning! 🚀**

*Last Updated: December 21, 2025*
