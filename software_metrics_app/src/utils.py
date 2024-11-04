import pandas as pd

def get_metrics_info():
    metrics_data = {
        "Metric": [
            "CBO", "DIT", "FanIn", "FanOut", "LCOM", "NOC", 
            "RFC", "WMC", "LOC", "Attributes", 
            "Attributes_Inherited", "Methods", 
            "Methods_Inherited", "Bugs"
        ],
        "Full Name": [
            "Coupling Between Objects", "Depth of Inheritance Tree", "FanIn", "FanOut", 
            "Lack of Cohesion in Methods", "Number of Children", "Response for a Class", 
            "Weighted Methods per Class", "Lines of Code", "Attributes", 
            "Attributes Inherited", "Methods", 
            "Methods Inherited", "Bugs"
        ],
        "Description": [
            "Measures the number of classes that the class is directly related to.",
            "Measures the maximum length of the path from a class to the root of the inheritance tree.",
            "Measures the number of classes that directly depend on a given class.",
            "Measures the number of classes that a given class directly depends on.",
            "Measures the degree to which methods of a class are related to each other.",
            "Counts the number of immediate subclasses of a class.",
            "Measures the number of methods that can be invoked in response to a message to an object of the class.",
            "Measures the complexity of a class by summing the complexities of its methods.",
            "Counts the number of lines in the source code, often excluding comments and blank lines.",
            "Counts the number of attributes (data members) in a class.",
            "Counts the number of attributes inherited from parent classes.",
            "Counts the number of methods defined in a class.",
            "Counts the number of methods inherited from parent classes.",
            "Counts the number of identified bugs or defects associated with a class."
        ]
    }
    return pd.DataFrame(metrics_data)
