# Week 6: YouTube Transcript Summarizer 🎬📝

## 📋 Overview

A LangChain-powered application that extracts and summarizes YouTube video transcripts using AI. This project demonstrates text processing, prompt engineering, and LangChain Expression Language (LCEL) to create intelligent video summaries in multiple styles.

## ✨ Features

- Extract transcripts from YouTube videos automatically
- Support for multiple caption formats (JSON3, VTT)
- Three summarization styles: Concise, Detailed, and Structured
- Text preprocessing and intelligent chunking
- LangSmith integration for observability
- Cost-effective token usage optimization

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- OpenAI API key
- (Optional) LangSmith API key for tracing

### Required Packages

```bash
pip install langchain langchain-community langchain-openai yt-dlp python-dotenv
```

### Environment Setup

Create a `.env` file in the project directory:

```env
OPENAI_API_KEY=sk-your-key-here
LANGSMITH_API_KEY=lsv2_your-key-here
LANGSMITH_TRACING_V2=true
LANGSMITH_PROJECT=YouTube-Transcript-Summarizer
```

## 🏗️ Architecture & Components

### 1. Transcript Extraction (`get_youtube_transcript`)

- Extracts captions using `yt-dlp`
- Supports both auto-generated and manual captions
- Handles JSON3 and VTT formats
- Returns clean, readable text

### 2. Text Preprocessing (`preprocess_text`)

- Removes extra whitespace
- Cleans special characters
- Fixes punctuation spacing
- Prepares text for LLM processing

### 3. Text Chunking (`chunk_text`)

- Splits large transcripts into manageable chunks
- Uses `RecursiveCharacterTextSplitter` for natural boundaries
- Maintains overlap between chunks for context preservation
- Default: 2000 chars per chunk, 200 char overlap

### 4. YouTubeSummarizer Class

Main class that orchestrates the summarization process:

**Methods:**

- `__init__(api_key, model)` - Initialize with OpenAI credentials
- `summarize_chunk(text, style)` - Summarize individual text chunks
- `summarize_full_transcript(transcript, style, chunk_size)` - Process entire video

**Summarization Styles:**

- **Concise**: 3-4 sentence summary
- **Detailed**: Overview + bullet points + conclusions
- **Structured**: What/Why/How/Outcomes format

### 5. Complete Pipeline (`summarize_youtube_video`)

End-to-end function that:

- Extracts YouTube transcript
- Initializes summarizer
- Generates summaries in specified style
- Returns results with metadata
- Optional LangSmith tracing for observability

## 💡 How It Works

### Workflow Diagram

1. YouTube URL → Extract Transcript
2. Preprocess Text → Clean & Normalize
3. Chunk Text → Split into Manageable Pieces
4. Summarize Chunks → Process with LLM
5. Combine Results → Final Summary

### Caption Format Handling

**JSON3 Format** (YouTube's compressed format):
- Automatically parsed and decoded
- Handles nested event structures

**VTT Format** (WebVTT subtitle format):
- Extracts clean text from timestamped captions
- Removes timing information

The code automatically detects and parses both formats.

## 🔧 Customization Guide

### Adjust Summarization Chunk Size

```python
summarize_youtube_video(url, style="detailed", chunk_size=3000)
```

### Create Custom Prompt Templates

```python
custom_prompt = ChatPromptTemplate.from_template(
    "Summarize this in technical terms: {text}"
)
```

### Change LLM Model

```python
summarizer = YouTubeSummarizer(api_key=api_key, model="gpt-4")
```

### Enable LangSmith Tracing

Set environment variables before running:

```env
```env
LANGSMITH_TRACING_V2=true
LANGSMITH_API_KEY=your-key-here
LANGSMITH_PROJECT=YouTube-Summarizer
```

## 🧪 Testing with YouTube Videos

### Recommended Test Videos

- **Educational**: TED talks, tutorials, lectures
- **Technical**: Conference talks, coding walkthroughs
- **News**: News clips, interviews
- **Creative**: Movie scenes, music videos with captions

**Important**: Videos must have English captions (auto-generated or manually added)

### Example Test URLs

```python
# Short educational video (5-10 min)
url = "https://www.youtube.com/watch?v=example1"

# Technical talk (20-30 min)
url = "https://www.youtube.com/watch?v=example2"
```

## 🔑 Key Concepts

### LangChain LCEL (LangChain Expression Language)

Chain components together elegantly:

```python
chain = prompt | llm | output_parser
result = chain.invoke({"input": text})
```

### Text Splitting Strategies

- **RecursiveCharacterTextSplitter**: Splits at natural boundaries (paragraphs, sentences, words)
- **Chunk Size**: Balance between context length and API cost
- **Overlap**: Maintain context across chunks (10% overlap is typical)

### Prompt Engineering for Summarization

- Be specific about output format
- Provide clear style examples
- Use structured outputs (bullet points, sections)
- Specify length constraints

## ⚠️ Common Issues & Solutions

### "No captions found"

- YouTube videos must have captions enabled
- Check if video has English subtitles
- Auto-generated captions are supported

### "OPENAI_API_KEY not found"

- Ensure `.env` file is in the notebook directory
- Check that `OPENAI_API_KEY` is set correctly
- Verify API key is active at https://platform.openai.com/api-keys

### "Rate limit exceeded"

- Reduce `chunk_size` to process fewer API calls
- Add delays between requests if processing multiple videos
- Consider using `gpt-3.5-turbo` for cost savings

### "Timeout connecting to YouTube"

- Check internet connection
- YouTube may be blocking yt-dlp; try updating: `pip install --upgrade yt-dlp`
- Try a different video

## 📊 Performance Considerations

### API Cost Estimation

| Model | Cost per 1K Tokens (Input) | Cost per 1K Tokens (Output) |
|-------|---------------------------|----------------------------|
| GPT-4 | $0.03 | $0.06 |
| GPT-3.5-turbo | $0.0005 | $0.0015 |

### Processing Time

- **Transcript extraction**: 5-15 seconds (depends on YouTube)
- **Preprocessing**: < 1 second
- **Summarization**: 10-30 seconds (LLM API latency)
- **Total**: 15-45 seconds per video

### Token Usage

- **Small video (5 min)**: ~1000-2000 tokens
- **Medium video (15 min)**: ~3000-5000 tokens
- **Large video (60 min)**: ~10000-15000 tokens

## 🚀 Next Steps & Challenges

### Beginner Challenges

- [ ] Summarize a 5-minute video in 3 different styles
- [ ] Export summaries to markdown or PDF
- [ ] Build a simple Streamlit UI for batch processing

### Intermediate Challenges

- [ ] Add multi-language support (translate summaries)
- [ ] Implement caching to avoid re-processing same URLs
- [ ] Create domain-specific prompts (tech, news, education)

### Advanced Challenges

- [ ] Process entire playlists automatically
- [ ] Build a knowledge graph from multiple summaries
- [ ] Add vector embeddings for semantic search
- [ ] Implement streaming responses
- [ ] Try different LLM providers (Claude, Gemini)

## 📚 Additional Resources

### Official Documentation

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Reference](https://platform.openai.com/docs)
- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- [LangSmith Documentation](https://docs.smith.langchain.com/)

### Related Topics

- **Prompt Engineering**: Learn to craft better LLM inputs
- **RAG (Retrieval-Augmented Generation)**: Week 4's project
- **Text Embeddings**: Semantic search and similarity
- **LLM Fine-tuning**: Custom model training

## 💬 Tips for Success

1. **Start Small**: Test with short videos first (5 minutes)
2. **Monitor Costs**: Keep track of API usage in OpenAI dashboard
3. **Experiment**: Try different prompt templates and styles
4. **Read Errors**: LLM and YouTube errors are usually descriptive
5. **Use LangSmith**: Trace runs to debug issues
6. **Ask Questions**: Don't hesitate to ask in live sessions!

## 📞 Support

- **Live Sessions**: Follow along for walkthrough and Q&A
- **Discord/Community**: Share your results and ask questions
- **Office Hours**: Debug specific issues with instructors
- **Documentation**: Check notebooks for inline comments

---

**Happy Summarizing! 🎬📝**

Questions? Ask during the live session or reach out to the community!