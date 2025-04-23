
from unstructured.partition.pdf import partition_pdf

raw_pdf_elements=partition_pdf(
    filename="/content/data/cj.pdf",
    strategy="hi_res",
    extract_images_in_pdf=True,
    extract_image_block_types=["Image", "Table"],
    extract_image_block_to_payload=False,
    extract_image_block_output_dir="extracted_data"
  )

raw_pdf_elements

Header=[]
Footer=[]
Title=[]
NarrativeText=[]
Text=[]
ListItem=[]


for element in raw_pdf_elements:
  if "unstructured.documents.elements.Header" in str(type(element)):
            Header.append(str(element))
  elif "unstructured.documents.elements.Footer" in str(type(element)):
            Footer.append(str(element))
  elif "unstructured.documents.elements.Title" in str(type(element)):
            Title.append(str(element))
  elif "unstructured.documents.elements.NarrativeText" in str(type(element)):
            NarrativeText.append(str(element))
  elif "unstructured.documents.elements.Text" in str(type(element)):
            Text.append(str(element))
  elif "unstructured.documents.elements.ListItem" in str(type(element)):
            ListItem.append(str(element))

NarrativeText

ListItem

img=[]
for element in raw_pdf_elements:
  if "unstructured.documents.elements.Image" in str(type(element)):
            img.append(str(element))

img[2]

raw_pdf_elements2=partition_pdf(
    filename="/content/data2/Retrieval-Augmented-Generation-for-NLP.pdf",
    strategy="hi_res",
    extract_images_in_pdf=True,
    extract_image_block_types=["Image", "Table"],
    extract_image_block_to_payload=False,
    extract_image_block_output_dir="extracted_data2"
  )

raw_pdf_elements2

img=[]
for element in raw_pdf_elements2:
  if "unstructured.documents.elements.Image" in str(type(element)):
            img.append(str(element))

img

tab=[]
for element in raw_pdf_elements2:
  if "unstructured.documents.elements.Table" in str(type(element)):
            tab.append(str(element))

tab[0]

NarrativeText=[]
for element in raw_pdf_elements2:
  if "unstructured.documents.elements.NarrativeText" in str(type(element)):
            NarrativeText.append(str(element))

ListItem=[]
for element in raw_pdf_elements2:
  if "unstructured.documents.elements.ListItem" in str(type(element)):
            ListItem.append(str(element))


len(tab)

tab[0]

len(img)

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Prompt
prompt_text = """You are an assistant tasked with summarizing tables for retrieval. \
    These summaries will be embedded and used to retrieve the raw table elements. \
    Give a concise summary of the table that is well optimized for retrieval. Table {element} """

prompt = ChatPromptTemplate.from_template(prompt_text)

import os
from google.colab import userdata
OPENAI_API_TOKEN=userdata.get('OPENAI_API_KEY')
os.environ["OPENAI_API_KEY"] = OPENAI_API_TOKEN

# Text summary chain
model = ChatOpenAI(temperature=0, model="gpt-4")

summarize_chain = {"element": lambda x: x} | prompt | model | StrOutputParser()

table_summaries = []

table_summaries=summarize_chain.batch(tab,{"max_concurrency": 5})

tab[0]

table_summaries[0]

img[0]

import base64
import os
from langchain_core.messages import HumanMessage

def encode_image(image_path):
    """Getting the base64 string"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def image_summarize(img_base64, prompt):
    """Make image summary"""


    chat = ChatOpenAI(model="gpt-4-vision-preview", max_tokens=1024)

    msg = chat.invoke(
        [
            HumanMessage(
                content=[
                    {"type": "text", "text": prompt},

                     {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{img_base64}"},
                    },
                ]
            )
        ]
    )
    return msg.content

def generate_img_summaries(path):
    """
    Generate summaries and base64 encoded strings for images
    path: Path to list of .jpg files extracted by Unstructured
    """

    # Store base64 encoded images
    img_base64_list = []

    # Store image summaries
    image_summaries = []

    # Prompt
    prompt = """You are an assistant tasked with summarizing images for retrieval. \
    These summaries will be embedded and used to retrieve the raw image. \
    Give a concise summary of the image that is well optimized for retrieval."""


    base64_image = encode_image(path)
    img_base64_list.append(base64_image)
    image_summaries.append(image_summarize(base64_image, prompt))

    return img_base64_list, image_summaries

fpath="/content/extracted_data2/figure-17-4.jpg"

img_base64_list,image_summaries=generate_img_summaries(fpath)

image_summaries[0]

