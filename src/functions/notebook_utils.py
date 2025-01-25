import ipywidgets as widgets
from IPython.display import display, clear_output
import time
import logging

# Configure the logger
def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    
    # Add the handler to the logger
    if not logger.hasHandlers():
        logger.addHandler(ch)
    
    return logger

# Timing decorator
def log_timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        logger = logging.getLogger(func.__module__)
        logger.info(f"Function {func.__name__} took {elapsed_time:.2f} seconds")
        return result
    return wrapper

def create_search_widget(entries):
    search_box = widgets.Text(
        description='Search:',
        placeholder='Type to search...',
        layout=widgets.Layout(width='300px')
    )
    
    output = widgets.Output()

    def on_search(change):
        with output:
            clear_output()
            search_term = change['new']
            
            if search_term == "*":
                print("All entries:")
                if isinstance(entries, dict):
                    for key, value in sorted(entries).items():
                        print(f"{key}: {value}")
                elif isinstance(entries, list):
                    for entry in sorted(entries):
                        print(entry)
            elif search_term:
                print(f"Results for '{search_term}':")
                if isinstance(entries, dict):
                    matches = {key: value for key, value in entries.items() if search_term.lower() in key.lower()}
                    if matches:
                        for key, value in sorted(matches).items():
                            print(f"{key}: {value}")
                    else:
                        print("No matching keys found.")
                elif isinstance(entries, list):
                    matches = [entry for entry in entries if search_term.lower() in entry.lower()]
                    if matches:
                        for match in sorted(matches):
                            print(f"{match}")
                    else:
                        print("No matching entries found.")
            else:
                print("Please enter a search term or '*' to see all options.")

    search_box.observe(on_search, names='value')
    display(search_box, output)
