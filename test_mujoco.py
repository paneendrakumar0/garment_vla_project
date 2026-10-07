import mujoco
import time

# Create a basic XML string defining an empty world with a light and a ground plane
xml = """
<mujoco>
  <worldbody>
    <light diffuse=".5 .5 .5" pos="0 0 3" dir="0 0 -1"/>
    <geom type="plane" size="1 1 0.1" rgba=".9 0 0 1"/>
  </worldbody>
</mujoco>
"""

# Load the model from the XML string
model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

print("MuJoCo Model Loaded Successfully!")
print(f"Number of Generalized Coordinates (DoF): {model.nq}")

# Step the simulation forward 10 times
for i in range(10):
    mujoco.mj_step(model, data)
    
print(f"Simulation time after 10 steps: {data.time:.3f} seconds")