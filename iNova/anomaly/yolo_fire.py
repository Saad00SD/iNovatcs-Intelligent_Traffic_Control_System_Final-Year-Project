from ultralytics import YOLO
import os

def run_fire_detection(video_path, output_path):
    model = YOLO(r'anomaly/MLModels/best.pt')
    
    # Run prediction and save the output
    results = model.predict(source=video_path, save=True, save_txt=False, project=os.path.dirname(output_path), name='predict', exist_ok=True)
    
    # The output is saved in a 'predict' folder
    predict_dir = os.path.join(os.path.dirname(output_path), 'predict')
    
    # Debug print statements
    print(f"Looking for output video in: {predict_dir}")
    if os.path.exists(predict_dir):
        files = os.listdir(predict_dir)
        print(f"Files in predict directory: {files}")
        
        for file in files:
            if file.endswith('.mp4'):
                output_file_path = os.path.join(predict_dir, file)
                print(f"Found output video: {output_file_path}")
                return output_file_path
    
    # If we get here, no output file was found
    print("No output video file found")
    return None