from pageindex import PageIndexClient
from dotenv import load_dotenv

load_dotenv()


def main():
    pageindex_client = PageIndexClient(index="vertex_ai/gemini-2.5-flash", chat="vertex_ai/gemini-2.5-flash")

    doc_id: dict[str, any] = pageindex_client.submit_document(
        file_path="ai-product-engineer-guide.pdf"
    )["doc_id"]

    query = "How many phases are there in this roadmap"

    for chunk in pageindex_client.chat(query, doc_id=doc_id, stream=True):
        print(chunk, end="", flush=True)

if __name__ == "__main__":
    main()


