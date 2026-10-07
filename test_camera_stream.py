import mujoco
import numpy as np
import cv2
import time

def main():
    try:
        model = mujoco.MjModel.from_xml_path("scene.xml")
        data = mujoco.MjData(model)
        
        # Let cloth settle
        for _ in range(100):
            mujoco.mj_step(model, data)
            
        renderer = mujoco.Renderer(model, 480, 640)
        renderer.update_scene(data, "overhead_cam")
        img = renderer.render()
        
        # Convert RGB to BGR for OpenCV
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imwrite("render.png", img_bgr)
        print("Render saved to render.png")
        
        # Enforce sleep to clear VRAM as per directive
        time.sleep(3)
    except Exception as e:
        print(f"Error: {e}")
        import sys
        sys.exit(1)

if __name__ == "__main__":
    main()
