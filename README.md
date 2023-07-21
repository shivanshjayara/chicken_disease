# chicken_disease

* utils folder:
    - This will contains those modules which we will frequently be using in the code.
    - Example: Reading yaml file, because every time we will be using this in many function.

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity: It is just a return type of a function **This we will call in the configuration manager file**
5. Update the configuration manager in src config  **This we will call in the pipeline file**
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml


- Data Ingestion
- Prepare base model
    **In image classification we don not require data validattion stage is not require because the image folders are in  correct format. But we can add if we require. It is general require for NLP and object detetction problem**
    **Fist we will build configuration for paths in config.yaml**
- Call back
    **We will not be creating any pipeline for this. We will use this inside the training piepline. This will actually help us in training**

- Model Evaluation: 
    **In evaluation we dont need any configuration.**
    **Here we check loss and accuracy**

- DVC:
    **DVC need git to be initialized.**
    **Use 'dvc repro' command to start execution**
    **Use 'dvc dag' command to see the piepline. Here we can see which stage is depemdemt on which stage.**
    