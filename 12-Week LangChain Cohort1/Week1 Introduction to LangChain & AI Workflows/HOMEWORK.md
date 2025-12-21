# 📝 Week 1 Homework Assignment

**12-Week LangChain Cohort - Week 1: Introduction to LangChain & AI Workflows**

---

## 📋 Assignment Overview

This homework consists of **16 questions** divided into 4 main sections. Each question is designed to reinforce the concepts you learned this week and build practical skills with LangChain.

### **Total Questions: 16**
- Section 1 (LLMs): 5 questions
- Section 2 (Prompts): 5 questions  
- Section 3 (Chains): 3 questions
- Section 4 (Tools): 3 questions

### **Estimated Time: 4-6 hours**

---

## ✅ Submission Guidelines

### What to Submit:
1. Completed Jupyter notebook with all code cells filled
2. All outputs visible (run all cells before submitting)
3. Your name and date at the top of the notebook
4. Brief comments explaining your approach (where asked)

### How to Submit:
- Save your completed notebook
- Ensure all cells have been executed
- Submit via [your submission platform/email]
- Include screenshot of key outputs if required

---

## 🤖 Section 1: LLMs (Language Models)

### **Question 1: Text Extraction from LLM Responses**

**Task:**
Change the code so it prints only the text answer (not the whole object). Show **two ways** you tried to get the text (one should be `response.content`). Say which way you liked best and why (1–2 sentences).

**What to Submit:**
- Short code snippet showing both methods
- One-sentence explanation of your preference

**Example Format:**
```python
# Method 1: Using .content
print(response.content)

# Method 2: [Your alternative method]
# ...

# My preference: I prefer Method 1 because...
```

**Learning Goal:** Understand different ways to extract text from LLM response objects and choose the most appropriate method.

---

### **Question 2: Temperature Parameter Experimentation**

**Task:**
Experiment with the `temperature` parameter. Run the same prompt with `temperature=0.0`, `0.7`, and `1.0`. For each value, record the model output and describe how the outputs differ in style or creativity.

**What to Submit:**
- Three outputs (one for each temperature value)
- Short comparison table (3–6 bullet points)

**Comparison Table Format:**
| Temperature | Output | Observations |
|-------------|--------|--------------|
| 0.0 | [Your output] | [Deterministic, consistent...] |
| 0.7 | [Your output] | [Balanced creativity...] |
| 1.0 | [Your output] | [More varied, creative...] |

**Learning Goal:** Understand how temperature affects LLM creativity and output variability.

**💡 Hint:** Use the same prompt (e.g., "Explain LangChain in 1 line") for all three temperatures to see clear differences.

---

### **Question 3: Error Handling Implementation**

**Task:**
Add simple error handling around the `llm.invoke()` call to catch missing API key or network errors. Show code that gracefully reports the failure to the user and **retries once**. Explain how your handler improves robustness.

**What to Submit:**
- Code snippet with try-except blocks
- 3–4 line explanation of robustness improvements

**Requirements:**
- ✅ Catch exceptions (API key errors, network issues)
- ✅ Print user-friendly error messages
- ✅ Implement retry logic (attempt once more)
- ✅ Return `None` or error message if both attempts fail

**Example Structure:**
```python
def safe_invoke(llm, prompt):
    try:
        # First attempt
        ...
    except Exception as e:
        # Handle error and retry
        ...
```

**Learning Goal:** Build production-ready code with proper error handling and retry mechanisms.

---

### **Question 4: Model Comparison**

**Task:**
Run the same prompt with `gpt-3.5-turbo` and another model you can access (for example `gpt-4o-mini` if you have it). Show both answers and write 2–3 lines recommending which model is better for short, one-line definitions and why.

**What to Submit:**
- Both model outputs
- Recommendation (2–3 sentences)

**Comparison Format:**
```
Model 1 (gpt-3.5-turbo): [Output]
Model 2 (gpt-4o-mini): [Output]

Recommendation: I recommend [model] for one-line definitions because...
```

**Learning Goal:** Understand the trade-offs between different models (speed vs quality, cost vs capability).

**💡 Note:** If you only have access to one model, compare `gpt-3.5-turbo` with different temperature settings instead.

---

### **Question 5: Temperature Testing & Selection**

**Task:**
Combine the temperature idea with a short test: ask "Explain LangChain in one line" three times in a row with `temperature=0.3`, `0.6`, and `0.9`. Save the three answers and pick which you like best. Say one reason why.

**What to Submit:**
- Three answers (one for each temperature)
- Your chosen favorite
- One-line reason for your choice

**Format:**
```
Temperature 0.3: [Output]
Temperature 0.6: [Output]
Temperature 0.9: [Output]

Favorite: [Temperature X]
Reason: [Your explanation]
```

**Learning Goal:** Develop intuition for choosing appropriate temperature values based on use case.

---

## 📋 Section 2: Prompts — Giving Context to LLMs

### **Question 1: Summarization Template**

**Task:**
Create a prompt template that asks the model to summarize a paragraph in one sentence.

**Requirements:**
- Write the template string with a `{paragraph}` placeholder
- Build the `PromptTemplate` with `from_template()`
- Call `prompt.format(...)` with a sample paragraph

**What to Submit:**
- Template string
- Formatted output

**Example:**
```python
template = "Summarize the following paragraph in one sentence: {paragraph}"
prompt = PromptTemplate.from_template(template)
# ... format and print
```

**Learning Goal:** Create reusable prompt templates with placeholders for dynamic content.

---

### **Question 2: Multi-Variable Template**

**Task:**
Make a template with **two variables**, `topic` and `tone`, for: "Explain {topic} in a {tone} style."

**Requirements:**
- Show the template creation
- Fill it with `topic="prompt engineering"` and `tone="simple"`
- Print the formatted prompt

**What to Submit:**
- Template code
- Printed formatted prompt

**Learning Goal:** Work with multiple variables in templates for more flexible prompts.

**💡 Bonus:** Try different combinations of topic and tone to see how versatile templates are!

---

### **Question 3: Missing Variable Error Handling**

**Task:**
Show what happens when a required variable is missing. Use the original template and call `prompt.format()` **without** the `text` variable.

**Requirements:**
- Run it and capture the error (or behavior)
- Write 2–3 lines explaining why the error occurs
- Explain how to avoid it

**What to Submit:**
- Error message (screenshot or text)
- Short explanation (2-3 lines)

**Example Explanation Format:**
```
Error Message: [The actual error]

Explanation:
• The error occurs because...
• Python raises [error type] when...
• To avoid this, always...
```

**Learning Goal:** Understand error handling for template variables and defensive programming.

---

### **Question 4: Few-Shot Learning Template**

**Task:**
Create a template that includes example few-shot pairs. For example:

**Instruction:** "Translate to French."

**Examples:** Include two input/output examples inside the template, then add `{text}` at the end for a new sentence.

**Requirements:**
- Build the template with embedded examples
- Print the formatted prompt for a new sentence

**What to Submit:**
- Complete template string with examples
- Final formatted prompt

**Template Structure:**
```
Instruction: Translate to French.

Examples:
Input: Hello
Output: Bonjour

Input: Good morning
Output: Bon matin

Now translate this:
Input: {text}
Output:
```

**Learning Goal:** Implement few-shot learning to guide model behavior with examples.

**💡 Tip:** Few-shot prompting is one of the most powerful techniques in prompt engineering!

---

### **Question 5: Prompt Validation**

**Task:**
Combine `PromptTemplate` with a simple prompt validation: write code that checks input length and refuses to format if the input is empty or too long (e.g., >1000 chars).

**Requirements:**
- Provide the validation function
- Show example outputs for:
  - (a) Valid input
  - (b) Invalid input (empty)
  - (c) Invalid input (too long)

**What to Submit:**
- Validation code
- Three example outputs

**Function Structure:**
```python
def validate_and_format(prompt_template, text_input):
    # Check 1: Empty input
    if not text_input or text_input.strip() == "":
        return "Error: Input cannot be empty"
    
    # Check 2: Too long
    if len(text_input) > 1000:
        return "Error: Input too long"
    
    # If valid, format
    return prompt_template.format(text=text_input)
```

**Learning Goal:** Build production-ready validation to prevent errors and wasted API calls.

---

## 🔗 Section 3: Chains — Combining Logic Steps

### **Question 1: Chain Execution and Text Extraction**

**Task:**
Run the snippet as-is and save the output. Then print the model text only (not the whole object).

**Requirements:**
- Show terminal output (or screenshot)
- One sentence showing how you printed just the text

**What to Submit:**
- Full output (showing the complete response object)
- Clean text-only output
- One sentence explanation

**Code Structure:**
```python
# Run the chain
result = chain.invoke({"text": "LangChain is awesome"})

# Show full output
print(result)

# Show text only
print(result.strip())  # For OpenAI completion models
```

**Learning Goal:** Understand chain execution and response handling.

**💡 Note:** For `OpenAI` (completion model), result is already a string. For `ChatOpenAI`, use `result.content`.

---

### **Question 2: Summarization Chain**

**Task:**
Change the prompt to ask for a short summary (1 sentence) instead of a translation. Run the chain and save the answer.

**Requirements:**
- Modify the template from translation to summarization
- Run the chain with sample text
- Display the output

**What to Submit:**
- New template string
- Chain output (summary)

**Example:**
```python
summary_prompt = PromptTemplate.from_template(
    "Summarize the following text in 1 sentence:\n\n{text}"
)
```

**Learning Goal:** Understand chain flexibility—same structure, different tasks.

---

### **Question 3: Multi-Model Chain**

**Task:**
Combine two different models in a chain: use `gpt-3.5-turbo-instruct` for translation and another available model for polishing (if you have it). Show both outputs and say which one looked better.

**Requirements:**
- First model: Translate text to French
- Second model: Polish the translation
- Compare outputs
- State preference with reason

**What to Submit:**
- Code for both chains
- Both outputs
- One-line preference statement

**Chain Structure:**
```
Input → Translation (Model 1) → Polishing (Model 2) → Final Output
```

**Learning Goal:** Build multi-step workflows using different models for different tasks.

**💡 Real-world application:** Draft generation → Review → Editing pipeline

---

## 🛠️ Section 4: Tools — Extending Model Capabilities

### **Question 1: Enhanced Weather Function**

**Task:**
Rewrite `get_weather` so it returns a more detailed reply (e.g., temperature and condition). Run it and show the new output.

**Requirements:**
- Add temperature information
- Add detailed weather condition
- Return formatted string

**What to Submit:**
- Updated function code
- Example output

**Enhanced Output Format:**
```
Weather in Mumbai:
   Temperature: 32°C
   Condition: Partly cloudy with high humidity
```

**Learning Goal:** Build more realistic and useful tools with detailed outputs.

---

### **Question 2: Input Validation for Tools**

**Task:**
Add input validation: if the city is empty, return "Please provide a city name." Demonstrate what happens when you call the tool with `""`.

**Requirements:**
- Validate that city is not empty or whitespace
- Return helpful error message for invalid input
- Show two example calls:
  - Valid city name
  - Empty string

**What to Submit:**
- Code with validation
- Two example calls and their outputs

**Validation Logic:**
```python
def get_weather(city: str) -> str:
    if not city or city.strip() == "":
        return "⚠️ Please provide a city name."
    # ... rest of function
```

**Learning Goal:** Build robust tools with input validation for production use.

---

### **Question 3: Test Harness**

**Task:**
Make a small test harness: write a list of cities `["Mumbai","Paris","Nowhere"]` and call `tool.invoke()` for each, collecting results into a list. Print the list.

**Requirements:**
- Test with multiple cities
- Collect all results in a list
- Display formatted output

**What to Submit:**
- Test code
- Printed list output

**Test Harness Structure:**
```python
test_cities = ["Mumbai", "Paris", "Nowhere"]
results = []

for city in test_cities:
    result = tool.invoke(city)
    results.append({"city": city, "weather": result})

print(results)
```

**Learning Goal:** Build automated tests to ensure tool reliability and catch edge cases.

**💡 Tip:** Test harnesses are essential for production applications!

---

## 🎯 Bonus Challenges (Optional)

Want to go further? Try these advanced exercises:

### **Bonus 1: Chain Pipeline**
Create a 3-step chain:
1. Translate text to English (any language input)
2. Summarize in 2-3 sentences
3. Extract 3 key points as bullet list

### **Bonus 2: Custom Tool**
Build a calculator tool that:
- Takes a math expression as string
- Evaluates it safely (use `eval()` with caution!)
- Returns the result
- Handles errors gracefully

### **Bonus 3: Advanced Prompt**
Create a prompt template that:
- Takes topic, audience, and length as variables
- Uses few-shot examples
- Validates all inputs
- Formats output consistently

---

## 📊 Grading Rubric

### Code Quality (40%)
- ✅ Code runs without errors
- ✅ Proper imports and setup
- ✅ Clean, readable code
- ✅ Appropriate comments

### Understanding (30%)
- ✅ Explanations demonstrate comprehension
- ✅ Appropriate use of parameters
- ✅ Correct implementation of concepts
- ✅ Thoughtful analysis of results

### Completeness (20%)
- ✅ All questions attempted
- ✅ All outputs visible
- ✅ Required formats followed
- ✅ Proper documentation

### Creativity (10%)
- ✅ Exploration beyond requirements
- ✅ Thoughtful examples
- ✅ Bonus challenges attempted
- ✅ Unique insights shared

---

## 💡 Tips for Success

### Before You Start:
1. ✅ Ensure your environment is set up correctly
2. ✅ Test your API key with a simple call
3. ✅ Read all questions first to plan your time
4. ✅ Keep the documentation handy

### While Working:
1. 💾 **Save frequently** - Don't lose your work!
2. 🧪 **Test incrementally** - Run each cell as you complete it
3. 📝 **Take notes** - Document your observations
4. 🔍 **Read errors carefully** - They often tell you exactly what's wrong
5. 🎯 **Start simple** - Get basic version working, then enhance

### Common Pitfalls to Avoid:
- ❌ Not running cells in order
- ❌ Forgetting to import required libraries
- ❌ Hardcoding API keys (use .env file!)
- ❌ Not reading error messages
- ❌ Skipping validation and error handling
- ❌ Copying without understanding

---

## 🆘 Getting Help

### If You're Stuck:

1. **Check the main notebook** - All solutions are documented with explanations
2. **Review error messages** - Read them carefully for clues
3. **Test components individually** - Isolate the problem
4. **Search documentation** - Links in README.md
5. **Ask specific questions** - Include error messages and code snippets

### Good Questions Include:
- What you were trying to accomplish
- What you expected to happen
- What actually happened (error message)
- What you've already tried
- Relevant code snippet

### Example:
> "I'm trying to create a prompt template with two variables (Q2), but I'm getting a KeyError. I expected it to format the prompt with both topic and tone, but it says 'tone' is missing. I've checked my code and both variables seem to be in the template. Here's my code: [code snippet]"

---

## 📅 Deadline & Submission

**Due Date:** [Your instructor will specify]

**Submission Method:** [Email/Platform/GitHub]

**Late Policy:** [Your instructor will specify]

---

## ✨ Final Thoughts

This homework is designed to reinforce your Week 1 learning and build muscle memory with LangChain fundamentals. Don't rush through it—take time to:

- **Understand each concept** before moving to the next
- **Experiment with variations** to deepen your understanding  
- **Document your learnings** for future reference
- **Ask questions** when you're confused

Remember: The goal is **learning**, not just completion. If you find yourself copying code without understanding it, slow down and make sure you grasp the concepts.

**You've got this! 🚀**

---

## 📚 Reference

### Quick Links:
- [Week 1 README](./README.md) - Complete week overview
- [Main Notebook](./Week1-lws_Student+HW.ipynb) - Lessons and solutions
- [LangChain Docs](https://python.langchain.com/) - Official documentation
- [OpenAI Docs](https://platform.openai.com/docs) - API reference

### Key Code Patterns:

**LLM Invocation:**
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
response = llm.invoke("Your prompt here")
print(response.content)
```

**Prompt Template:**
```python
from langchain_core.prompts import PromptTemplate
template = "Your template with {variable}"
prompt = PromptTemplate.from_template(template)
formatted = prompt.format(variable="value")
```

**Chain:**
```python
chain = prompt | llm
result = chain.invoke({"variable": "value"})
```

**Tool:**
```python
from langchain_core.tools import Tool
tool = Tool(name="MyTool", func=my_function, description="...")
output = tool.invoke("input")
```

---

**Happy Coding! May your models be accurate and your prompts be clear! 🎓✨**

*Week 1 Homework - 12-Week LangChain Cohort*
