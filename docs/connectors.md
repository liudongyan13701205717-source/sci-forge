# 科学数据连接器（46 个）

> 本文档由 `sciforge/science/` 自动生成，记录所有已注册连接器。
> 46 个连接器覆盖 7 大领域，均以公开接口访问。

## 领域分布

| 领域 | 数量 | 连接器 id |
| --- | --- | --- |
| chemistry | 6 | `chembl`, `pubchem`, `chebi`, `bindingdb`, `gtopdb`, `surechembl` |
| datasets | 4 | `zenodo`, `doaj`, `openaire`, `huggingface` |
| genomics | 7 | `ensembl`, `eutils`, `mygene`, `myvariant`, `clinvar`, `dbsnp`, `gnomad` |
| literature | 12 | `openalex`, `arxiv`, `biorxiv`, `crossref`, `europepmc`, `pubmed`, `semantic-scholar`, `unpaywall`, `core`, `opencitations-coci`, `cnki`, `wanfang` |
| omics | 6 | `arrayexpress`, `depmap`, `expression-atlas`, `geo`, `gtex`, `hpa` |
| pathways | 5 | `biogrid`, `intact`, `kegg`, `opentargets`, `reactome` |
| proteins | 6 | `uniprot`, `rcsb-pdb`, `pdbe`, `alphafold`, `interpro`, `sifts` |
| **合计** | **46** | |

## 连接器总表

| # | ID | 名称 | 领域 | 描述 | 需要 key |
| --- | --- | --- | --- | --- | --- |
| 1 | `chembl` | ChEMBL | chemistry | Bioactive drug-like compounds | 否 | chemistry.py:9 |
| 2 | `pubchem` | PubChem | chemistry | Chemical molecules and bioactivities | 否 | chemistry.py:31 |
| 3 | `chebi` | ChEBI | chemistry | Chemical entities of biological interest | 否 | chemistry.py:59 |
| 4 | `bindingdb` | BindingDB | chemistry | Protein-ligand binding affinities | 否 | chemistry.py:81 |
| 5 | `gtopdb` | GuideToPharmacology | chemistry | Drug targets and ligands | 否 | chemistry.py:103 |
| 6 | `surechembl` | SureChEMBL | chemistry | Patent chemistry | 否 | chemistry.py:125 |
| 7 | `zenodo` | Zenodo | datasets | Zenodo research data | 否 | datasets.py:9 |
| 8 | `doaj` | DOAJ | datasets | Directory of Open Access Journals | 否 | datasets.py:31 |
| 9 | `openaire` | OpenAIRE | datasets | OpenAIRE research graph | 否 | datasets.py:54 |
| 10 | `huggingface` | Hugging Face | datasets | Hugging Face datasets | 否 | datasets.py:78 |
| 11 | `ensembl` | Ensembl | genomics | Ensembl genome browser | 否 | genomics.py:9 |
| 12 | `eutils` | NCBI eutils | genomics | NCBI Entrez utilities | 否 | genomics.py:30 |
| 13 | `mygene` | MyGene.info | genomics | Gene annotation service | 否 | genomics.py:61 |
| 14 | `myvariant` | MyVariant.info | genomics | Variant annotation service | 否 | genomics.py:83 |
| 15 | `clinvar` | ClinVar | genomics | Clinical variant interpretations | 否 | genomics.py:105 |
| 16 | `dbsnp` | dbSNP | genomics | Short genetic variations | 否 | genomics.py:136 |
| 17 | `gnomad` | gnomAD | genomics | Genome aggregation database | 否 | genomics.py:167 |
| 18 | `openalex` | OpenAlex | literature | OpenAlex works catalog | 否 | literature.py:22 |
| 19 | `arxiv` | arXiv | literature | arXiv preprints | 否 | literature.py:46 |
| 20 | `biorxiv` | bioRxiv | literature | bioRxiv preprints | 否 | literature.py:71 |
| 21 | `crossref` | Crossref | literature | Crossref metadata | 否 | literature.py:92 |
| 22 | `europepmc` | Europe PMC | literature | Europe PMC literature | 否 | literature.py:122 |
| 23 | `pubmed` | PubMed | literature | PubMed biomedical literature | 否 | literature.py:143 |
| 24 | `semantic-scholar` | Semantic Scholar | literature | Semantic Scholar papers | 否 | literature.py:178 |
| 25 | `unpaywall` | Unpaywall | literature | Unpaywall OA metadata (DOI lookup) | 否 | literature.py:226 |
| 26 | `core` | CORE | literature | CORE aggregator (需配置 CORE_API_KEY) | 否 | literature.py:253 |
| 27 | `opencitations-coci` | OpenCitations COCI | literature | OpenCitations COCI citation data (DOI lookup) | 否 | literature.py:279 |
| 28 | `cnki` | CNKI | literature | 中国知网 (需配置 CNKI_API_URL) | 否 | literature.py:348 |
| 29 | `wanfang` | Wanfang | literature | 万方数据 (需配置 WANFANG_API_URL) | 否 | literature.py:358 |
| 30 | `arrayexpress` | ArrayExpress | omics | Functional genomics experiments | 否 | omics.py:9 |
| 31 | `depmap` | DepMap | omics | Cancer dependency map | 否 | omics.py:30 |
| 32 | `expression-atlas` | Expression Atlas | omics | Gene expression patterns | 否 | omics.py:51 |
| 33 | `geo` | GEO | omics | Gene Expression Omnibus | 否 | omics.py:72 |
| 34 | `gtex` | GTEx | omics | Genotype-Tissue Expression | 否 | omics.py:103 |
| 35 | `hpa` | Human Protein Atlas | omics | Tissue protein expression | 否 | omics.py:128 |
| 36 | `biogrid` | BioGRID | pathways | Protein-protein interactions | 否 | pathways.py:9 |
| 37 | `intact` | IntAct | pathways | Molecular interactions | 否 | pathways.py:40 |
| 38 | `kegg` | KEGG | pathways | Kyoto Encyclopedia of Genes and Genomes | 否 | pathways.py:61 |
| 39 | `opentargets` | Open Targets | pathways | Target-disease associations | 否 | pathways.py:85 |
| 40 | `reactome` | Reactome | pathways | Pathway database | 否 | pathways.py:107 |
| 41 | `uniprot` | UniProt | proteins | UniProt protein knowledgebase | 否 | proteins.py:9 |
| 42 | `rcsb-pdb` | RCSB PDB | proteins | Protein Data Bank | 否 | proteins.py:44 |
| 43 | `pdbe` | PDBe | proteins | Protein Data Bank in Europe | 否 | proteins.py:67 |
| 44 | `alphafold` | AlphaFold DB | proteins | AlphaFold protein structures | 否 | proteins.py:89 |
| 45 | `interpro` | InterPro | proteins | Protein families and domains | 否 | proteins.py:110 |
| 46 | `sifts` | PDBe SIFTS | proteins | Structure integration with function | 否 | proteins.py:133 |

## 按领域分组

### chemistry

| ID | 名称 | 描述 | 需要 key |
| --- | --- | --- | --- |
| `chembl` | ChEMBL | Bioactive drug-like compounds | 否 |
| `pubchem` | PubChem | Chemical molecules and bioactivities | 否 |
| `chebi` | ChEBI | Chemical entities of biological interest | 否 |
| `bindingdb` | BindingDB | Protein-ligand binding affinities | 否 |
| `gtopdb` | GuideToPharmacology | Drug targets and ligands | 否 |
| `surechembl` | SureChEMBL | Patent chemistry | 否 |

### datasets

| ID | 名称 | 描述 | 需要 key |
| --- | --- | --- | --- |
| `zenodo` | Zenodo | Zenodo research data | 否 |
| `doaj` | DOAJ | Directory of Open Access Journals | 否 |
| `openaire` | OpenAIRE | OpenAIRE research graph | 否 |
| `huggingface` | Hugging Face | Hugging Face datasets | 否 |

### genomics

| ID | 名称 | 描述 | 需要 key |
| --- | --- | --- | --- |
| `ensembl` | Ensembl | Ensembl genome browser | 否 |
| `eutils` | NCBI eutils | NCBI Entrez utilities | 否 |
| `mygene` | MyGene.info | Gene annotation service | 否 |
| `myvariant` | MyVariant.info | Variant annotation service | 否 |
| `clinvar` | ClinVar | Clinical variant interpretations | 否 |
| `dbsnp` | dbSNP | Short genetic variations | 否 |
| `gnomad` | gnomAD | Genome aggregation database | 否 |

### literature

| ID | 名称 | 描述 | 需要 key |
| --- | --- | --- | --- |
| `openalex` | OpenAlex | OpenAlex works catalog | 否 |
| `arxiv` | arXiv | arXiv preprints | 否 |
| `biorxiv` | bioRxiv | bioRxiv preprints | 否 |
| `crossref` | Crossref | Crossref metadata | 否 |
| `europepmc` | Europe PMC | Europe PMC literature | 否 |
| `pubmed` | PubMed | PubMed biomedical literature | 否 |
| `semantic-scholar` | Semantic Scholar | Semantic Scholar papers | 否 |
| `unpaywall` | Unpaywall | Unpaywall OA metadata (DOI lookup) | 否 |
| `core` | CORE | CORE aggregator (需配置 CORE_API_KEY) | 否 |
| `opencitations-coci` | OpenCitations COCI | OpenCitations COCI citation data (DOI lookup) | 否 |
| `cnki` | CNKI | 中国知网 (需配置 CNKI_API_URL) | 否 |
| `wanfang` | Wanfang | 万方数据 (需配置 WANFANG_API_URL) | 否 |

### omics

| ID | 名称 | 描述 | 需要 key |
| --- | --- | --- | --- |
| `arrayexpress` | ArrayExpress | Functional genomics experiments | 否 |
| `depmap` | DepMap | Cancer dependency map | 否 |
| `expression-atlas` | Expression Atlas | Gene expression patterns | 否 |
| `geo` | GEO | Gene Expression Omnibus | 否 |
| `gtex` | GTEx | Genotype-Tissue Expression | 否 |
| `hpa` | Human Protein Atlas | Tissue protein expression | 否 |

### pathways

| ID | 名称 | 描述 | 需要 key |
| --- | --- | --- | --- |
| `biogrid` | BioGRID | Protein-protein interactions | 否 |
| `intact` | IntAct | Molecular interactions | 否 |
| `kegg` | KEGG | Kyoto Encyclopedia of Genes and Genomes | 否 |
| `opentargets` | Open Targets | Target-disease associations | 否 |
| `reactome` | Reactome | Pathway database | 否 |

### proteins

| ID | 名称 | 描述 | 需要 key |
| --- | --- | --- | --- |
| `uniprot` | UniProt | UniProt protein knowledgebase | 否 |
| `rcsb-pdb` | RCSB PDB | Protein Data Bank | 否 |
| `pdbe` | PDBe | Protein Data Bank in Europe | 否 |
| `alphafold` | AlphaFold DB | AlphaFold protein structures | 否 |
| `interpro` | InterPro | Protein families and domains | 否 |
| `sifts` | PDBe SIFTS | Structure integration with function | 否 |

## 可选环境变量

| 变量 | 影响的连接器 | 未配置时 |
| --- | --- | --- |
| `CORE_API_KEY` | `core` | 返回空结果，不报错 |
| `CNKI_API_URL` | `cnki` | 返回空结果，不报错 |
| `WANFANG_API_URL` | `wanfang` | 返回空结果，不报错 |
| `SCI_FORGE_OFFLINE=1` | 全部 | 强制离线，测试与 CI 使用 |
