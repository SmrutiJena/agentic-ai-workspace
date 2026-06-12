print("======================Hello, World!==================")

from sentence_transformers  import SentenceTransformer

sentence_transformer_model = SentenceTransformer('all-MiniLM-L6-v2')

my_text = "This is a test sentence for embedding."
my_text1 = "Smruti"
embedding = sentence_transformer_model.encode(my_text1)
embedding1 = sentence_transformer_model.encode(my_text1)
print("Embedding for the text:", embedding)
print("Embedding for the text-1:", embedding1)

from langchain_openai import OpenAIEmbeddings
OpenAI_embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
my_sentence="This is an example sentence for embedding using OpenAI's model."
my_sentence_embedding_openai = OpenAI_embedding_model.embed_query(my_sentence)
my_sentence_embedding_openai
len(my_sentence_embedding_openai)