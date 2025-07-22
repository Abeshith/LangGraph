# Curie Radiation Documents

This folder contains a curated collection of historical documents about Marie Curie and her groundbreaking work with radiation and radioactivity. These documents serve as a sample knowledge base for RAG (Retrieval-Augmented Generation) examples and experiments.

## 📚 What's Included

This collection provides comprehensive coverage of Marie Curie's life, scientific discoveries, and lasting impact on science and medicine. The documents are perfect for testing and demonstrating RAG systems, document retrieval, and question-answering applications.

## 📁 Document Overview

### Historical Biography
- **`1_curie_bio.txt`** - Comprehensive biography of Marie Curie
  - Early life in Warsaw, Poland
  - Education and move to Paris
  - Meeting Pierre Curie and their collaboration
  - Personal challenges and triumphs

### Scientific Discoveries
- **`2_radiation_discovery.txt`** - The discovery of radiation and radioactivity
  - Initial observations and experiments
  - Understanding radioactive elements
  - Theoretical frameworks developed

- **`3_radium_application.txt`** - Applications and uses of radium
  - Industrial applications
  - Early medical uses
  - Commercial developments

- **`8_curie_lab_notes.txt`** - Laboratory work and experimental methods
  - Research methodologies
  - Scientific techniques and innovations
  - Collaborative research approaches

- **`9_impact_on_chemistry.txt`** - Impact on the field of chemistry
  - New understanding of atomic structure
  - Influence on periodic table development
  - Chemical isolation techniques

### Medical and Healthcare Impact
- **`4_radioactivity_medical.txt`** - Medical applications of radioactivity
  - Early therapeutic uses
  - Diagnostic applications
  - Safety considerations and protocols

- **`6_radiotherapy_origin.txt`** - Origins of radiotherapy
  - First cancer treatments using radiation
  - Development of medical protocols
  - Training of medical professionals

- **`7_modern_radiation.txt`** - Modern radiation applications
  - Contemporary medical uses
  - Advanced therapeutic techniques
  - Current safety standards

- **`10_healthcare_advances.txt`** - Healthcare advances attributed to Curie's work
  - Long-term impact on medical practice
  - Modern diagnostic techniques
  - Preventive medicine applications

### Recognition and Legacy
- **`5_nobel_prize.txt`** - Nobel Prize achievements
  - First Nobel Prize in Physics (1903)
  - Second Nobel Prize in Chemistry (1911)
  - Historical significance of dual awards
  - Recognition of women in science

## 🎯 Use Cases for RAG Systems

### Educational Applications
- **Historical Research**: Query specific events, dates, and achievements
- **Scientific Education**: Learn about radioactivity and nuclear physics
- **Biography Studies**: Explore personal and professional life details
- **Timeline Analysis**: Understand chronological development of discoveries

### Technical Applications
- **Document Retrieval**: Test semantic search capabilities
- **Question Answering**: Build knowledge-based Q&A systems
- **Information Synthesis**: Combine information from multiple documents
- **Fact Verification**: Cross-reference claims across documents

### Example Queries for Testing

#### Biographical Queries
- "When and where was Marie Curie born?"
- "How did Marie and Pierre Curie meet?"
- "What challenges did Marie Curie face as a woman in science?"
- "What happened to Marie Curie later in her life?"

#### Scientific Queries
- "What is radioactivity and how was it discovered?"
- "How did the Curies isolate radium?"
- "What were the key laboratory techniques used by Marie Curie?"
- "How did Curie's work impact our understanding of chemistry?"

#### Medical and Application Queries
- "How is radiation used in modern medicine?"
- "What were the first medical applications of radioactivity?"
- "How did radiotherapy develop from Curie's discoveries?"
- "What safety measures are important when working with radiation?"

#### Legacy and Impact Queries
- "Why did Marie Curie win two Nobel Prizes?"
- "How did Curie's work influence modern healthcare?"
- "What is Marie Curie's lasting impact on science?"
- "How did her discoveries change medical treatment?"

## 🔍 Document Processing Tips

### For RAG Implementation
1. **Chunking Strategy**: Documents can be split by paragraphs or topics
2. **Metadata Enhancement**: Add document type, topic, and date information
3. **Cross-References**: Many documents reference similar concepts
4. **Entity Extraction**: Extract people, places, dates, and scientific terms

### Preprocessing Recommendations
```python
# Example preprocessing approach
def preprocess_curie_documents(file_path):
    # Load document
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add metadata based on filename
    metadata = {
        "source": file_path,
        "topic": extract_topic_from_filename(file_path),
        "document_type": "historical_text",
        "subject": "marie_curie",
        "domain": "science_history"
    }
    
    return content, metadata

def extract_topic_from_filename(filename):
    topic_mapping = {
        "1_curie_bio.txt": "biography",
        "2_radiation_discovery.txt": "scientific_discovery",
        "3_radium_application.txt": "applications",
        "4_radioactivity_medical.txt": "medical_applications",
        "5_nobel_prize.txt": "recognition",
        "6_radiotherapy_origin.txt": "medical_development",
        "7_modern_radiation.txt": "modern_applications",
        "8_curie_lab_notes.txt": "laboratory_work",
        "9_impact_on_chemistry.txt": "scientific_impact",
        "10_healthcare_advances.txt": "healthcare_impact"
    }
    
    return topic_mapping.get(filename.split('/')[-1], "general")
```

## 📊 Content Statistics

### Document Characteristics
- **Total Documents**: 10 text files
- **Content Type**: Historical and scientific narrative
- **Language**: English
- **Format**: Plain text (.txt)
- **Average Length**: ~200-300 words per document
- **Topics Covered**: Biography, science, medicine, legacy

### Key Entities Present
- **People**: Marie Curie, Pierre Curie, Henri Becquerel
- **Places**: Warsaw, Paris, Sorbonne University
- **Scientific Terms**: Radioactivity, radium, polonium, uranium
- **Institutions**: Nobel Committee, universities, laboratories
- **Medical Terms**: Radiotherapy, cancer treatment, diagnosis

## 🚀 Getting Started with These Documents

### Quick RAG Implementation
```python
# Example: Load documents for RAG
import os
from pathlib import Path

def load_curie_documents():
    documents = []
    doc_folder = Path("Curie_Radiation_Documents")
    
    for file_path in doc_folder.glob("*.txt"):
        content, metadata = preprocess_curie_documents(file_path)
        documents.append({
            "content": content,
            "metadata": metadata,
            "id": file_path.stem
        })
    
    return documents

# Use with your RAG system
def setup_curie_rag():
    documents = load_curie_documents()
    
    # Create embeddings and vector store
    # (Implementation depends on your RAG framework)
    vectorstore = create_vector_store(documents)
    
    return vectorstore
```

### Sample RAG Workflow
1. **Load Documents** → Process all 10 text files
2. **Create Embeddings** → Generate vector representations
3. **Build Vector Store** → Index documents for retrieval
4. **Test Queries** → Try example questions
5. **Evaluate Results** → Check relevance and accuracy

## 💡 Tips for Effective Use

### Best Practices
1. **Document Relationships**: Consider connections between documents
2. **Context Preservation**: Maintain historical and scientific context
3. **Multi-Document Queries**: Test queries that span multiple sources
4. **Temporal Awareness**: Consider chronological aspects of information

### Common Challenges
1. **Historical Context**: Ensure modern applications relate to historical discoveries
2. **Scientific Accuracy**: Verify technical information across sources
3. **Biography vs. Science**: Balance personal and professional information
4. **Citation Tracking**: Track which documents provide specific information

## 📖 Educational Value

This document collection provides excellent learning opportunities for:
- **History of Science**: Understanding scientific progress and discovery
- **Women in STEM**: Learning about pioneering female scientists
- **Medical History**: Tracing the development of modern medical techniques
- **RAG Development**: Practicing with coherent, related documents

## 🔬 Scientific Learning Outcomes

After working with these documents, you'll understand:
- The discovery and nature of radioactivity
- Early applications of radiation in medicine
- The development of modern radiotherapy
- Marie Curie's scientific methodology and approach
- The historical context of early 20th-century physics and chemistry

This collection serves as both a technical resource for RAG development and an educational journey through one of science's most important discoveries and the remarkable woman who made it possible.
