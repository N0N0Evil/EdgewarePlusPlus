from videoprops import get_video_properties
base_path = "EdgeWare\\resource\\vid\\"
test_files = ["test.mov", "test.mp4", "test.webm"]
for file in test_files:
    try:
        print(get_video_properties(base_path + file)['duration'])
    except:
        print(get_video_properties(base_path + file)['tags']['DURATION'])
    
    print("  ")
    print("  ")