# Week 4: PDF Document Summarizer (RAG Project)

## 📚 Introduction to RAG (Retrieval-Augmented Generation)

Welcome to Week 4 of the LangChain Cohort! This week, you'll build a powerful PDF Document Summarizer using RAG (Retrieval-Augmented Generation) - one of the most important patterns in AI applications today.

### What is RAG?

RAG is an AI architecture that combines:
- **Retrieval**: Finding relevant information from your documents
- **Generation**: Using LLMs to generate accurate answers based on that information

This approach enables LLMs to answer questions about YOUR specific documents, going beyond their training data.

---

## 🎯 Learning Objectives

By the end of this session, you will be able to:

1. **Load and Process PDFs** - Extract text from PDF documents using PyPDFLoader
2. **Implement Text Chunking** - Split documents into optimal chunks for processing
3. **Create Vector Embeddings** - Convert text into semantic vectors using OpenAI
4. **Build Vector Stores** - Store and search embeddings efficiently with FAISS
5. **Design RAG Pipelines** - Create end-to-end question-answering systems
6. **Use LangSmith** - Monitor and debug your LangChain applications
7. **Build Interactive Systems** - Create chat interfaces for document Q&A

---

## 🛠️ Project Overview

### What You'll Build

An intelligent PDF Question-Answering system that:
- Loads PDF documents and extracts content
- Splits text into manageable, semantic chunks
- Converts chunks into vector embeddings
- Stores embeddings in a FAISS vector database
- Retrieves relevant context for user queries
- Generates accurate answers using GPT models
- Provides an interactive chat interface

### Real-World Applications

- **Legal Document Analysis** - Query contracts, agreements, and legal documents
- **Research Paper Summarization** - Extract insights from academic papers
- **Policy & Insurance Documents** - Understand complex policy terms
- **Technical Documentation** - Search through manuals and guides
- **Knowledge Management** - Build corporate knowledge bases

---

## 📁 Project Structure

```
Week 4 PDF Document Summarizer/
├── PDF Document Summarizer (RAG Project) - Students.ipynb  # Main notebook
├── README.md                                                # This file
├── requirements.txt                                         # Python dependencies
├── Session - PDF Document Summarizer.pdf                    # Session slides
├── HDFC-Life-Group-Term-Life-Policy.pdf                    # Sample PDF 1
├── HDFC-Life-Sampoorna-Jeevan-101N158V04-Policy-Document (1).pdf  # Sample PDF 2
└── HDFC-Life-Sanchay-Plus-Life-Long-Income-Option-101N134V19-Policy-Document.pdf  # Sample PDF 3
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API Key
- Basic understanding of LangChain (from Weeks 1-3)
- Jupyter Notebook or VS Code with Jupyter extension

### Installation

#### Option 1: Using requirements.txt (Recommended)

1. **Install all dependencies at once**

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes all necessary packages:
- `langchain` - Core LangChain library
- `langchain-openai` - OpenAI integrations
- `langchain-community` - Community integrations
- `pypdf` - PDF processing
- `faiss-cpu` - Vector similarity search
- `python-dotenv` - Environment variable management
- `langsmith` - LangChain monitoring and debugging

#### Option 2: Manual Installation

1. **Install Required Packages individually**

```bash
pip install langchain langchain-openai langchain-community pypdf faiss-cpu python-dotenv langsmith
```

2. **Set Up Environment Variables**

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langsmith_api_key_here  # Optional for LangSmith
LANGCHAIN_TRACING_V2=true                       # Enable LangSmith tracing
LANGCHAIN_PROJECT=pdf-summarizer-week4          # Project name in LangSmith
```

3. **Verify Installation**

```python
import langchain
print(langchain.__version__)
```

---

## 📖 Notebook Structure

### Part 1: Environment Setup
- Installing dependencies
- Importing libraries
- Setting up API keys

### Part 2: Loading PDF Documents
- Understanding PyPDFLoader
- Loading PDF files
- Exploring document metadata
- Handling different PDF formats

**Key Concepts:**
- Document loaders
- Metadata preservation
- Page tracking

### Part 3: Text Chunking
- Why chunking is necessary
- Understanding chunk_size and chunk_overlap
- Using RecursiveCharacterTextSplitter
- Analyzing chunk statistics

**Key Concepts:**
- Token limits
- Semantic chunking
- Context preservation
- Optimal chunk sizes

### Part 4: Creating Embeddings
- What are vector embeddings?
- Understanding semantic similarity
- Using OpenAI's text-embedding-3-small model
- Testing embeddings with cosine similarity

**Key Concepts:**
- Vector representations
- Semantic search vs keyword search
- Embedding dimensions (1536D)
- Cosine similarity

### Part 5: Building FAISS Vector Store
- Introduction to FAISS (Facebook AI Similarity Search)
- Creating and populating vector stores
- Performing similarity searches
- Understanding similarity scores

**Key Concepts:**
- Vector databases
- Efficient similarity search
- Retrieval algorithms
- Saving and loading vector stores

### Part 6: Building the RAG Pipeline
- RAG architecture overview
- Setting up retrievers
- Designing prompt templates
- Building chains with LCEL (LangChain Expression Language)
- Testing the complete pipeline

**Key Concepts:**
- Retrieval-Augmented Generation
- Context injection
- Prompt engineering for RAG
- Chain construction

### Part 7: Interactive Chat Interface
- Building a chat function
- Handling user input
- Batch question processing
- Error handling

**Key Concepts:**
- Interactive systems
- User experience design
- Source attribution

---

## 🔑 Key Technologies

### LangChain Components

| Component | Purpose | Used For |
|-----------|---------|----------|
| `PyPDFLoader` | PDF Loading | Extracting text from PDF documents |
| `RecursiveCharacterTextSplitter` | Text Chunking | Splitting documents into chunks |
| `OpenAIEmbeddings` | Embeddings | Converting text to vectors |
| `FAISS` | Vector Store | Storing and searching embeddings |
| `ChatOpenAI` | LLM | Generating answers |
| `ChatPromptTemplate` | Prompts | Structuring LLM instructions |
| `StrOutputParser` | Output | Parsing LLM responses |

### External Tools

- **FAISS**: Facebook's efficient similarity search library
- **OpenAI API**: For embeddings and chat completions
- **LangSmith**: Monitoring and debugging (introduced this week!)
- **Python-dotenv**: Environment variable management

---

## 💡 Important Concepts

### Chunking Strategy

```python
RecursiveCharacterTextSplitter(
    chunk_size=1000,        # Characters per chunk
    chunk_overlap=200       # Overlap between chunks
)
```

**Why these values?**
- `chunk_size=1000`: Balances context and specificity
- `chunk_overlap=200`: Maintains context across boundaries

**Experimentation:**
- Too small (e.g., 500): Loses context, more chunks
- Too large (e.g., 3000): May exceed token limits
- No overlap: Risk of losing information at boundaries

### Vector Embeddings

```python
OpenAIEmbeddings(model="text-embedding-3-small")
```

- **Dimensions**: 1536D vector space
- **Purpose**: Semantic representation of text
- **Similarity**: Cosine similarity measures relevance

### RAG Pipeline Flow

```
📄 User Question
    ↓
🔍 Retrieve Relevant Chunks (Vector Search)
    ↓
📝 Inject into Prompt Template
    ↓
🤖 LLM Generates Answer
    ↓
✅ Return Answer + Sources
```

---

## 🧪 Exercises & Practice

### Beginner Level

1. **Load a PDF**: Load one of the sample PDFs and print the number of pages
2. **Chunk Analysis**: Experiment with different chunk_size values (500, 1000, 2000)
3. **Simple Query**: Ask a basic question about the document
4. **View Sources**: Display the source chunks used for an answer

### Intermediate Level

1. **Optimize Chunking**: Find the optimal chunk_size for your PDF
2. **Similarity Testing**: Compare semantic vs keyword similarity
3. **Custom Prompts**: Design better prompt templates
4. **Multiple Queries**: Test with 5-10 different questions

### Advanced Level

1. **Multi-PDF Support**: Load and query multiple PDFs simultaneously
2. **Citation System**: Add page number citations to answers
3. **Conversational Memory**: Implement follow-up question handling
4. **Performance Metrics**: Measure retrieval accuracy and speed

---

## 🏆 Homework Challenges

Choose one or more challenges to extend your learning:

### 1. Multi-PDF Support (Medium)
Build a system that can:
- Load multiple PDF documents
- Identify which PDF each answer comes from
- Allow users to select specific documents to query

**Hint**: Add metadata tags to distinguish documents

### 2. Citation System (Hard)
Enhance answers with:
- Specific page numbers
- Paragraph references
- Format: "According to page 5, paragraph 2..."

**Hint**: Use document metadata from PyPDFLoader

### 3. Conversational Memory (Medium-Hard)
Add conversation history:
- Remember previous questions and answers
- Handle follow-up questions ("Tell me more")
- Maintain context across turns

**Hint**: Use ConversationBufferMemory from LangChain

### 4. Streamlit UI (Easy-Medium)
Create a web interface with:
- PDF upload functionality
- Chat-like interface
- Source display panel
- Download conversation history

**Hint**: Use `streamlit` library

### 5. Semantic Chunking (Hard)
Improve chunking by:
- Detecting topic boundaries
- Preserving paragraph structure
- Using semantic similarity for splits

**Hint**: Research LangChain's SemanticChunker

---

## 🐛 Common Issues & Solutions

### Issue 1: PDF Loading Errors
**Problem**: "File not found" or encoding errors

**Solutions:**
- Use absolute file paths
- Check file permissions
- Verify PDF isn't corrupted or encrypted
- Try different PDF loaders (PDFPlumber, UnstructuredPDFLoader)

### Issue 2: Empty or Poor Retrievals
**Problem**: Retrieved chunks aren't relevant

**Solutions:**
- Adjust chunk_size and chunk_overlap
- Increase k value in retriever (e.g., k=5)
- Improve query phrasing
- Check embedding model compatibility

### Issue 3: API Rate Limits
**Problem**: "Rate limit exceeded" errors

**Solutions:**
- Add retry logic with exponential backoff
- Reduce batch sizes
- Use rate limiting libraries
- Consider caching embeddings

### Issue 4: Out of Memory
**Problem**: FAISS crashes with large PDFs

**Solutions:**
- Process PDFs in batches
- Use disk-based FAISS index
- Reduce chunk count
- Consider cloud vector databases

---

## 📊 Understanding LangSmith

This week introduces **LangSmith** - LangChain's observability platform.

### What is LangSmith?

LangSmith helps you:
- **Debug**: See exactly what's happening in your chains
- **Monitor**: Track performance and costs
- **Evaluate**: Test and improve RAG quality
- **Collaborate**: Share runs with team members

### Setting Up LangSmith

```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your_langsmith_key"
os.environ["LANGCHAIN_PROJECT"] = "pdf-summarizer-week4"
```

### What to Look For in LangSmith

- **Traces**: Full execution path of your chains
- **Token Usage**: Track costs and optimize
- **Latency**: Identify slow components
- **Errors**: Debug failures quickly

**Access**: https://smith.langchain.com

---

## 🎓 Additional Resources

### Official Documentation
- [LangChain Documentation](https://python.langchain.com)
- [FAISS GitHub](https://github.com/facebookresearch/faiss)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)
- [LangSmith Documentation](https://docs.smith.langchain.com)

### Recommended Reading
- "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (Research Paper)
- LangChain RAG Cookbook
- FAISS Performance Tuning Guide

### Video Tutorials
- LangChain RAG Tutorial Series
- Building Production RAG Systems
- FAISS Deep Dive

### Community
- LangChain Discord
- GitHub Discussions
- Stack Overflow #langchain tag

---

## 🔄 Next Steps

### Week 5 Preview: AI Email Assistant
Building on RAG fundamentals, you'll:
- Create email classification systems
- Generate automated responses
- Build email workflow automation

### Advanced RAG Topics (Future Sessions)
- Hybrid Search (Vector + Keyword)
- Re-ranking strategies
- Custom embeddings
- Multi-modal RAG (text + images)
- RAG evaluation metrics
- Production deployment

---

## ✅ Learning Checklist

Mark your progress as you complete each section:

- [ ] Environment setup complete
- [ ] Successfully loaded a PDF
- [ ] Understood chunking strategy
- [ ] Created embeddings and tested similarity
- [ ] Built FAISS vector store
- [ ] Constructed complete RAG pipeline
- [ ] Tested interactive chat interface
- [ ] Set up LangSmith monitoring
- [ ] Completed at least one homework challenge
- [ ] Experimented with different parameters

---

## 🎉 Congratulations!

You've completed one of the most important modules in the LangChain course. RAG is the foundation for countless AI applications:

- ✅ Customer support chatbots
- ✅ Internal knowledge bases
- ✅ Document analysis tools
- ✅ Research assistants
- ✅ Legal document review

**The skills you've learned this week scale to:**
- Millions of documents
- Multiple concurrent users
- Production-grade applications
- Mission-critical systems

### Keep Building! 🚀

The best way to master RAG is to build with it. Try different documents, experiment with parameters, and extend the basic system with your own features.

---

## 📝 Notes

- Sample PDFs provided are HDFC Life insurance policy documents
- Great for testing complex, multi-page PDF handling
- Contains technical and legal terminology
- Perfect for demonstrating RAG capabilities

---

## 🤝 Need Help?

If you encounter issues:

1. Check the **Common Issues** section above
2. Review LangSmith traces for debugging
3. Consult the official LangChain documentation
4. Ask in the course discussion forum
5. Reach out to instructors

---

---

## 🎯 Quick Start Guide (5 Minutes)

**New to this project? Start here!**

### Step 1: Install Everything (2 min)
```bash
pip install -r requirements.txt
```

### Step 2: Set Your API Key (1 min)
Create a `.env` file:
```
OPENAI_API_KEY=sk-your-key-here
```

### Step 3: Open the Notebook (30 sec)
```bash
jupyter notebook "PDF Document Summarizer (RAG Project) - Session_File.ipynb"
```

### Step 4: Run All Cells (1 min)
- Click "Kernel" → "Restart & Run All"
- Or press `Shift + Enter` through each cell

### Step 5: Start Asking Questions! (30 sec)
```python
chat_with_pdf(rag_chain, retriever)
```

**That's it!** You now have a working PDF Q&A system! 🎉

---

## 💰 Cost Calculator

**How much will this session cost me?**

### Typical Session Breakdown:
| Activity | API Calls | Approximate Cost |
|----------|-----------|------------------|
| Processing 1 PDF (50 pages) | ~100 embedding calls | $0.02 |
| Creating vector store | One-time cost | $0.05 |
| 10 test questions | 10 LLM + embedding calls | $0.05 |
| Interactive chat (20 questions) | 20 LLM calls | $0.10 |
| **Total for complete session** | | **~$0.20-0.30** |

**💡 Cost-Saving Tips:**
1. **Save your vector store** - Don't re-embed the same PDF
2. **Use the Session file** - It already has outputs to review
3. **Start with smaller PDFs** - Practice with 10-20 page documents
4. **Batch your questions** - Test multiple queries at once

**Free tier users:** OpenAI gives $5 free credit - enough for ~15-20 complete sessions!

---

## 🎨 Visual Learning: The Complete RAG Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    USER ASKS A QUESTION                      │
│              "What are the policy benefits?"                 │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│               STEP 1: CONVERT QUESTION TO VECTOR             │
│   OpenAI Embeddings: "What are policy benefits?"             │
│   → [0.23, -0.45, 0.67, ..., 0.12] (1536 dimensions)        │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│         STEP 2: SEARCH FAISS VECTOR DATABASE                 │
│   Compare query vector with all chunk vectors                │
│   Find top 3 most similar chunks (cosine similarity)         │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 3: RETRIEVE RELEVANT CHUNKS                │
│   Chunk 1: "The policy provides following benefits..."       │
│   Chunk 2: "Death benefit includes sum assured..."           │
│   Chunk 3: "Maturity benefits are calculated as..."          │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 4: BUILD CONTEXT PROMPT                    │
│   System: "You are a helpful assistant. Use context..."      │
│   Context: [Chunk 1] + [Chunk 2] + [Chunk 3]                │
│   Question: "What are the policy benefits?"                  │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│            STEP 5: LLM GENERATES ANSWER                      │
│   GPT-3.5-turbo processes prompt                             │
│   Generates answer based on retrieved chunks                 │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 6: RETURN FINAL ANSWER                     │
│   "The policy provides: 1) Death benefit 2) Maturity..."     │
│   Sources: Pages 3, 5, 7                                     │
└─────────────────────────────────────────────────────────────┘
```

---

## 🧩 Understanding the Code: Key Components

### Component 1: Document Loader
```python
# What it does: Extracts text from PDF
loader = PyPDFLoader("policy.pdf")
documents = loader.load()  # Each page becomes a Document object

# Documents contain:
# - page_content: The actual text
# - metadata: {source: "policy.pdf", page: 0}
```

### Component 2: Text Splitter
```python
# What it does: Breaks large text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Max 1000 chars per chunk
    chunk_overlap=200     # 200 chars overlap between chunks
)
chunks = splitter.split_documents(documents)
```

**Why overlap?** Imagine this text split at 1000 chars:
```
Chunk 1: "...The policy covers accidental death and provides
Chunk 2: benefits up to Rs. 10 lakhs..."
```
Without overlap, "provides benefits" is split! With overlap:
```
Chunk 1: "...The policy covers accidental death and provides benefits up to Rs."
Chunk 2: "provides benefits up to Rs. 10 lakhs..."
```
Now both chunks have complete information! ✅

### Component 3: Embeddings
```python
# What it does: Converts text to numbers (vectors)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Example:
text = "life insurance policy"
vector = embeddings.embed_query(text)
# Result: [0.023, -0.145, 0.891, ..., 0.234] (1536 numbers)
```

### Component 4: Vector Store
```python
# What it does: Stores vectors and enables fast search
vectorstore = FAISS.from_documents(chunks, embeddings)

# Internally does:
# 1. Convert each chunk to vector
# 2. Build search index
# 3. Store vectors + original text
```

### Component 5: RAG Chain
```python
# What it does: Connects everything together
rag_chain = (
    {"context": retriever | format_docs, "input": lambda x: x["input"]}
    | prompt | llm | StrOutputParser()
)

# Reads as:
# 1. Get question → retrieve chunks → format as text
# 2. Fill prompt template with context + question
# 3. Send to LLM
# 4. Parse response as string
```

---

## 🎯 Parameter Tuning Guide

### When to Adjust chunk_size

**Use SMALLER chunks (500-700) when:**
- ✅ Your PDF has short, focused sections (FAQs, lists)
- ✅ You need very precise answers
- ✅ Questions are specific and narrow

**Use LARGER chunks (1200-1500) when:**
- ✅ Your PDF has long, complex explanations
- ✅ Context matters (legal docs, research papers)
- ✅ Concepts span multiple paragraphs

### When to Adjust k (number of retrieved chunks)

**Use k=1-2 when:**
- ✅ Your questions have single, clear answers
- ✅ You want fast responses
- ✅ Your chunks are large and comprehensive

**Use k=5-7 when:**
- ✅ Questions might have multi-faceted answers
- ✅ Information is spread across document
- ✅ You want comprehensive coverage

### When to Adjust temperature

**Use temperature=0 when:**
- ✅ You need consistent, factual answers (default for RAG)
- ✅ Accuracy is critical
- ✅ Users expect the same answer every time

**Use temperature=0.3-0.7 when:**
- ✅ You want slightly varied phrasing
- ✅ Creative summarization is okay
- ✅ Exact wording isn't critical

---

## 🔍 Debugging Tips

### Problem: "My answers are generic and don't use the PDF"

**Diagnosis:**
1. Check if chunks are being retrieved:
```python
docs = retriever.invoke("your question")
print(f"Retrieved {len(docs)} chunks")
for doc in docs:
    print(doc.page_content[:200])
```

2. Check retrieval quality:
```python
results = vectorstore.similarity_search_with_score("your question", k=3)
for doc, score in results:
    print(f"Score: {score}")  # Lower is better
```

**Fix:** If scores > 1.0, your question might not match the document content.

### Problem: "System is slow"

**Diagnosis:**
- Each API call takes time
- Embedding creation is slowest part

**Fixes:**
1. Save vector store: `vectorstore.save_local("my_store")`
2. Load instead of recreating: `FAISS.load_local("my_store", embeddings)`
3. Reduce k value
4. Use smaller PDFs for testing

### Problem: "Getting 'API key not found' error"

**Diagnosis:**
```python
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("OPENAI_API_KEY"))  # Should print your key
```

**Fix:** 
- Ensure `.env` file is in the same directory as notebook
- Check for typos in variable name
- Restart kernel after creating `.env`

---

## 📚 Session File vs Student File

This project includes two notebooks:

### Session File (`PDF Document Summarizer (RAG Project) - Session_File.ipynb`)
- ✅ **Complete with outputs** - See what results should look like
- ✅ **Fully documented** - Every cell has detailed explanations
- ✅ **Ready to run** - Just add your API key
- 📝 **Use this for:** Learning, reference, review

### Student File (`PDF Document Summarizer (RAG Project) - Students.ipynb`)
- 🎯 **Exercise format** - TODOs and hints
- 🧩 **Learn by doing** - Fill in the code yourself
- 💪 **Skill building** - Practice what you learned
- 📝 **Use this for:** Homework, practice, assessment

**Recommended approach:**
1. Review Session File first to understand concepts
2. Try Student File to test your knowledge
3. Compare your solution with Session File
4. Experiment with both!

---

**Happy Learning! 📚✨**

*Last Updated: December 21, 2025*
