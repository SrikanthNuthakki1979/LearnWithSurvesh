# 📧 Week 5: AI Email Assistant with LangChain - Student Guide

## 🎯 What You'll Build

An intelligent AI Email Assistant that:
- 📩 Generates professional email replies automatically
- 🎨 Adapts communication style (formal, friendly, brief, detailed, empathetic)
- 🧠 Remembers conversation context across multiple emails
- 📊 Processes large batches of emails
- 💼 Works with real Gmail/Outlook exports
- 🔐 Maintains separate conversation threads

---

## ⚡ Quick Start (5 minutes)

### 1. Install Requirements
```bash
pip install langchain langchain-openai python-dotenv pandas
```

### 2. Get API Key
- Go to https://platform.openai.com/
- Create account (free $5 credit)
- Go to Settings → API Keys
- Generate new secret key

### 3. Create .env File
Create file named `.env` in same folder as notebook:
```
OPENAI_API_KEY=sk-your-key-here
```

### 4. Run Notebook
- Open `Week5_AI_Email_Assistant_STUDENT_Class_File.ipynb`
- Run cells from top to bottom
- See AI generate professional emails!

---

## 📚 What You'll Learn

| Topic | What | Duration |
|-------|------|----------|
| **Setup** | Libraries, API setup, LLM initialization | 10 min |
| **Data** | Email structure, datasets, sample data | 10 min |
| **Chains** | Prompt templates, LCEL syntax | 15 min |
| **Functions** | Email reply generation, error handling | 15 min |
| **Customization** | 5 communication tones | 10 min |
| **Memory** | Thread management, conversation context | 20 min |
| **Real Emails** | Parse Gmail, .eml files, batch processing | 15 min |

**Total Time: ~95 minutes**

---

## 🗂️ Notebook Structure

### Part 1: Foundation (STEPS 1-3)
- Import libraries
- Initialize OpenAI LLM
- Create sample email dataset

### Part 2: Basic Features (STEPS 4-6)
- Build prompt template
- Create email reply function
- Process batch of emails

### Part 3: Advanced Features (STEPS 7-8)
- Customize communication tone
- Implement conversation memory
- Show thread isolation

### Part 4: Production (BONUS)
- Parse real .eml files
- Complete workflow demo
- Challenge exercises

---

## 🎮 Three Ways to Use

### Option 1: Learn the Basics (20 min)
```python
# Single email reply
email = sample_emails[0]
reply = generate_email_reply(email)
print(reply['reply_body'])
```

### Option 2: Batch Processing (30 min)
```python
# Process all 5 sample emails
for email in sample_emails:
    reply = generate_email_reply(email)
    print(f"Generated reply for: {email['sender_name']}")
```

### Option 3: Complete Production (60 min)
```python
# Export your Gmail → Parse → Generate → Save
emails = parse_eml_directory("./my_emails/")
for email in emails:
    reply = generate_reply_with_memory(email, thread_id=f"thread-{email['id']}")
    # Use the reply in your application
```

---

## 🔑 Key Concepts Explained

### 1. **Chain (Pipeline)**
```
Email Data → PromptTemplate → OpenAI LLM → Professional Reply
```
Using LCEL: `prompt | llm`

### 2. **Memory (Context)**
```
Email 1: "Need pricing info"
↓ Stored in memory
Email 2: "And do you have discounts?"
↓ AI remembers email 1
Reply 2: References pricing mentioned earlier ✓
```

### 3. **Thread (Conversation)**
```
Same Thread: "support-ticket-001"
├─ Email 1: Customer asks question
├─ Reply 1: AI responds
├─ Email 2: Customer follows up
└─ Reply 2: AI responds, remembering Email 1

Different Thread: "sales-proposal-001"
└─ Completely separate memory!
```

### 4. **Tone (Personality)**
```python
tone="formal"     # Professional, structured
tone="friendly"   # Warm, approachable
tone="brief"      # Concise, to the point
tone="detailed"   # Comprehensive
tone="empathetic" # Understanding, caring
```

---

## 📊 Core Functions Reference

### 1. `generate_email_reply(email_data)`
**Basic email reply generation**
```python
reply = generate_email_reply(email, your_name="Sarah")
print(reply['reply_body'])
```

### 2. `generate_personalized_reply(email_data, tone="friendly")`
**Reply with custom tone**
```python
reply = generate_personalized_reply(email, tone="empathetic")
```

### 3. `generate_reply_with_memory(email_data, thread_id="ticket-123")`
**Reply with conversation context**
```python
reply = generate_reply_with_memory(email, thread_id="support-101")
```

### 4. `get_session_history(thread_id)`
**Access thread memory**
```python
history = get_session_history("ticket-123")
print(f"Messages in thread: {len(history.messages)}")
```

### 5. `parse_eml_file(filepath)`
**Parse single Gmail export**
```python
email = parse_eml_file("message.eml")
```

### 6. `parse_eml_directory(folder_path)`
**Batch parse all Gmail exports**
```python
emails = parse_eml_directory("./gmail_exports/")
```

---

## ⚠️ Before You Start

### ✅ Required
- Python 3.8+ installed
- OpenAI account (free tier is fine)
- API key in `.env` file
- 15 minutes of time

### ⚠️ Warnings
- **Cost**: Each email ~$0.001 (free tier = 500 test emails)
- **Rate Limit**: 3 requests/min on free tier
- **API Key**: Never share or commit to GitHub
- **Data**: Email contents sent to OpenAI servers

### 💡 Tips
- Run cells one at a time
- Read error messages - they help!
- Test with sample emails first
- Save successful results
- Join Discord for help

---

## 🎯 Success Checklist

By the end, you should be able to:

- [ ] Set up OpenAI API and get it working
- [ ] Explain what a prompt template is
- [ ] Understand LCEL chain syntax (|)
- [ ] Generate professional email replies
- [ ] Customize tone of responses
- [ ] Explain how conversation memory works
- [ ] Show thread isolation (multiple conversations)
- [ ] Parse real emails from Gmail
- [ ] Process batch of emails
- [ ] Save results to CSV
- [ ] Identify production improvements needed

---

## 🚀 Challenge Exercises

### Challenge 1: Tone Explorer ⭐
Try generating the same email in all 5 tones:
```python
email = sample_emails[1]
for tone in ["formal", "friendly", "brief", "detailed", "empathetic"]:
    reply = generate_personalized_reply(email, tone=tone)
    print(f"\n{tone.upper()}:\n{reply['reply']}")
```

### Challenge 2: Memory Tester ⭐⭐
Create a conversation thread with 3 emails:
```python
emails = [
    {"id": 1, "body": "Can you help with pricing?", ...},
    {"id": 2, "body": "And what about discounts?", ...},
    {"id": 3, "body": "When can we start?", ...}
]
for email in emails:
    reply = generate_reply_with_memory(email, thread_id="conversation")
```

### Challenge 3: Gmail Processor ⭐⭐
Export your own Gmail folder and process it:
```python
emails = parse_eml_directory("./my_gmail_exports/")
print(f"Parsed {len(emails)} emails")
for email in emails:
    reply = generate_email_reply(email)
```

### Challenge 4: Custom Tone ⭐⭐⭐
Add a new tone (e.g., "humorous", "casual"):
```python
personalization_styles["humorous"] = "Use light humor while remaining professional"
# Then use it:
reply = generate_personalized_reply(email, tone="humorous")
```

### Challenge 5: API Endpoint ⭐⭐⭐⭐
Build a Flask API around the email assistant:
```python
from flask import Flask, request
app = Flask(__name__)

@app.route('/generate-reply', methods=['POST'])
def generate():
    email = request.json
    reply = generate_email_reply(email)
    return reply
```

---

## 🆘 If Something Goes Wrong

### Error: "ModuleNotFoundError"
**Solution:**
```bash
pip install langchain langchain-openai python-dotenv pandas
```

### Error: "Invalid API key"
**Solution:**
1. Check `.env` file exists in same folder as notebook
2. Verify key is correct: `OPENAI_API_KEY=sk-...`
3. Restart kernel: Kernel → Restart
4. Test: `print(os.getenv("OPENAI_API_KEY"))`

### Error: "RateLimitError"
**Solution:**
- Wait 1 minute and try again
- Upgrade OpenAI plan for higher limits
- Add `import time; time.sleep(1)` between calls

### Other Issues
- Check [Debugging Guide](NOTEBOOK_ENHANCEMENTS.md) in notebook
- Review common issues section
- Ask instructor in Discord

---

## 📖 Learning Resources

### In This Notebook
- Detailed docstrings for every function
- Inline comments for every code block
- Real-world examples
- Challenge exercises
- Complete summary

### External Resources
- **LangChain Docs**: https://python.langchain.com/
- **OpenAI API**: https://platform.openai.com/docs/
- **Python Email**: https://docs.python.org/3/library/email.html
- **GitHub**: https://github.com/

### Getting Help
- 💬 **Discord**: Instructor and peers
- 📧 **Email**: Your instructor
- 📚 **Documentation**: Read error messages carefully
- 🔍 **Google**: Search the error message
- 🎥 **Videos**: YouTube LangChain tutorials

---

## 🏆 What You'll Be Able to Do

### After This Week
- ✅ Generate professional emails automatically
- ✅ Understand LangChain architecture
- ✅ Use OpenAI API effectively
- ✅ Implement conversation memory
- ✅ Process real Gmail exports

### Career Benefits
- 🚀 Valuable AI/ML skill
- 💼 Automatable routine task
- 📈 Scalable solution for business
- 💻 Production-ready code
- 🔧 Modern tool expertise

---

## 📝 Session Notes

### Session 1: Foundations
- [ ] Understand LLMs and prompts
- [ ] Set up OpenAI API
- [ ] Initialize ChatOpenAI
- [ ] Create first prompt template

### Session 2: Basic Features
- [ ] Build email reply chain
- [ ] Generate replies for sample emails
- [ ] Understand error handling
- [ ] Export results to CSV

### Session 3: Advanced Features
- [ ] Customize tone and style
- [ ] Understand conversation memory
- [ ] Create multi-turn conversations
- [ ] Isolate different threads

### Session 4: Production Ready
- [ ] Parse real .eml files
- [ ] Build complete workflow
- [ ] Complete challenge exercise
- [ ] Plan next project

---

## 🎁 Bonus Material

- Real workflow demo with Gmail exports
- Thread isolation demonstration
- Challenge exercises (5 levels)
- Debugging guide
- Deployment roadmap
- Business use cases

---

## 📊 Quick Stats

- **Lines of Code**: 500+
- **Functions**: 7 main functions
- **Sample Emails**: 5 realistic examples
- **Communication Tones**: 5 different styles
- **Documentation**: 100+ comments
- **Challenges**: 5 progressive exercises

---

## ✨ Pro Tips

1. **Run one cell at a time** - It's easier to debug
2. **Test with sample emails first** - Before using your data
3. **Read error messages carefully** - They tell you exactly what's wrong
4. **Save successful results** - Build your portfolio
5. **Experiment boldly** - Break things and learn!
6. **Read the comments** - They explain the "why" not just "what"
7. **Try all the tones** - See how they differ
8. **Create your own threads** - Understand memory better
9. **Ask questions** - Instructors love engaged students
10. **Share your results** - Show what you built!

---

## 🎓 Your Learning Journey

```
START: ❌ Don't know about AI email automation
  ↓
STEP 1-2: ✅ Understand basics, get API working
  ↓
STEP 3-4: ✅ Generate single email replies
  ↓
STEP 5-6: ✅ Batch process multiple emails
  ↓
STEP 7: ✅ Customize tone and style
  ↓
STEP 8-9: ✅ Implement memory, handle threads
  ↓
BONUS: ✅ Parse real emails, complete workflow
  ↓
CHALLENGES: ✅ Build advanced features
  ↓
END: 🚀 Ready to deploy production system!
```

---

## 🎉 Final Words

This notebook teaches you **practical AI skills** that are:
- ✅ In-demand in job market
- ✅ Applicable to real business problems
- ✅ Scalable to production
- ✅ Modern and cutting-edge
- ✅ Fun to learn and implement!

**You're building something real. You're learning something valuable. You're joining the AI revolution.**

---

**Ready to build? Let's go! 🚀**

Open the notebook and run the first cell!

---

*Created by Learn With Sarvesh*
*Week 5 - AI Email Assistant with LangChain*
*December 28, 2025*
