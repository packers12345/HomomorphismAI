from UI import create_app
import time

def get_data_from_gui():
    # Start the Tkinter GUI application
    app, root = create_app()

    # Function to close the GUI after some time
    def close_gui():
        time.sleep(10)  # Allow some time to interact with the GUI
        root.quit()  # Stop the GUI event loop

    # Start the GUI event loop in a separate thread
    import threading
    thread = threading.Thread(target=close_gui)
    thread.start()
    
    root.mainloop()

    # Retrieve the data after the GUI has been closed
    try:
        data = app.get_data()
        print(f"Data retrieved: {data}")
        return data
    except RuntimeError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    # Invoke the function to start the GUI and get data
    data_array = get_data_from_gui()
    print(f"Stored Data: {data_array}")
