import streamlit as st
from multi_page_app.multi_page import MultiPage
from multi_page_app.page_summary import page_project_summary_body
from multi_page_app.Mildew_and_Healthy_Visualizer import page_cells_visualizer_body
from multi_page_app.Mildew_detector import page_mildew_detector_body
from multi_page_app.project_hypothesis import page_project_hypothesis_body
from multi_page_app.ml_performance import page_ml_performance_metrics

app = MultiPage(app_name= "Detection of Diseased Leaves")

app.add_page("Quick Project Summary", page_project_summary_body)
app.add_page("Cherry leave Visualizer", page_cells_visualizer_body)
app.add_page("Mildew Detection", page_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run() 

