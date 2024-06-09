import matplotlib.pyplot as plt

def create_fig1():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)

    # Adding the steps in the flowchart with more details
    steps = [
        ("Soil Sample Collection", "Collect soil samples from various sites with different environmental conditions."),
        ("Initial Soil Testing", "Perform basic soil tests to determine initial properties (e.g., moisture content, density)."),
        ("Advanced Laboratory Testing", "Conduct advanced tests to characterize soil behavior under varied moisture and stress conditions."),
        ("Data Analysis", "Analyze test data to identify patterns, behaviors, and key parameters affecting soil performance."),
        ("Model Development", "Develop and refine the BBM to incorporate findings from the data analysis."),
        ("Numerical Simulations", "Use numerical tools (e.g., FLAC, Python) to simulate soil behavior with the refined model."),
        ("Model Validation", "Validate the refined model with additional laboratory and field tests."),
        ("Implementation", "Apply the validated model to real-world geotechnical problems and projects.")
    ]
    y_positions = list(range(12, -2, -2))
    
    for i, ((step, detail), y) in enumerate(zip(steps, y_positions)):
        ax.text(5, y, step, ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightblue', edgecolor='black', boxstyle='round,pad=0.5'))
        ax.text(5, y-0.5, detail, ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.5'))
        if i < len(steps) - 1:
            ax.arrow(5, y - 1.5, 0, -1.5, head_width=0.3, head_length=0.3, fc='black', ec='black')
    
    ax.axis('off')
    return fig

fig1 = create_fig1()
fig1.savefig("BBM_Refinement_Process_Flowchart_Enhanced.png")
plt.show()

import matplotlib.pyplot as plt

def create_fig2():
    fig, ax = plt.subplots(figsize=(12, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Adding eco-friendly techniques with descriptions
    techniques = [
        ("Bio-Based Polymers", "Polymers derived from natural sources used to stabilize soil by enhancing cohesion and reducing permeability."),
        ("Microbial-Induced Calcite Precipitation (MICP)", "Utilize bacteria (e.g., Sporosarcina pasteurii) to precipitate calcite and bind soil particles, improving strength and durability.")
    ]
    y_positions = [7, 3]
    
    for (technique, detail), y in zip(techniques, y_positions):
        ax.text(5, y, technique, ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightgreen', edgecolor='black', boxstyle='round,pad=0.5'))
        ax.text(5, y-0.5, detail, ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.5'))
        ax.arrow(5, y - 1, 0, -2, head_width=0.3, head_length=0.3, fc='black', ec='black')
        
    ax.text(5, 0.5, "Field Trials", ha='center', va='center', fontsize=12, bbox=dict(facecolor='lightyellow', edgecolor='black', boxstyle='round,pad=0.5'))
    ax.text(5, 0, "Evaluate the effectiveness of techniques in real-world conditions (e.g., soil stability, environmental impact).", ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', boxstyle='round,pad=0.5'))
    
    ax.axis('off')
    return fig

fig2 = create_fig2()
fig2.savefig("Eco_Friendly_Soil_Stabilization_Techniques_Enhanced.png")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

def create_fig3():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

    # Initial Soil Model
    ax1.set_title("Initial Soil and Structure Model")
    initial_data = np.random.random((100, 100))  # Simulated data for initial model
    cax1 = ax1.imshow(initial_data, cmap='viridis')
    fig.colorbar(cax1, ax=ax1, orientation='vertical')
    ax1.annotate('High Stress Area', xy=(70, 70), xytext=(60, 80),
                 arrowprops=dict(facecolor='white', shrink=0.05), fontsize=10, color='white')
    ax1.set_xlabel('X Position')
    ax1.set_ylabel('Y Position')

    # Stabilized Soil Model
    ax2.set_title("Stabilized Soil Model")
    stabilized_data = np.random.random((100, 100))  # Simulated data for stabilized model
    cax2 = ax2.imshow(stabilized_data, cmap='inferno')
    fig.colorbar(cax2, ax=ax2, orientation='vertical')
    ax2.annotate('Improved Stability', xy=(70, 70), xytext=(60, 80),
                 arrowprops=dict(facecolor='white', shrink=0.05), fontsize=10, color='white')
    ax2.set_xlabel('X Position')
    ax2.set_ylabel('Y Position')

    return fig

fig3 = create_fig3()
fig3.savefig("Finite_Element_Modeling_Results_Enhanced.png")
plt.show()
