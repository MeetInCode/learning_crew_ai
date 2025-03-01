from crewai_tools import YoutubeChannelSearchTool
import os 


os.environ['GOOGLE_API_KEY'] = os.getenv("GEMINI_API_KEY")
yt_tool = YoutubeChannelSearchTool(
    config=dict(
        llm=dict(
            provider="google", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="gemini/gemini-1.5-flash",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    ),
    youtube_channel_handle='@krishnaik06'
)