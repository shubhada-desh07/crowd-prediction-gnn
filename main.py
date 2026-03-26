import torch
from yolo_detector import get_live_detections
from temple_graph import get_temple_graph
from model import CrowdGNN
from utils import count_people_per_zone, get_risk, check_alert


def main():
    model = CrowdGNN()
    model.eval()

    print("🚀 Starting Live System (Press Q to exit)\n")

    # store unique IDs (for tracking)
    seen_ids = set()

    for detections, frame in get_live_detections():

        if len(detections) == 0:
            continue

        # 🔁 Remove duplicate IDs
        unique_detections = []

        for item in detections:
            if len(item) == 3:
                cx, cy, track_id = item

                if track_id not in seen_ids:
                    seen_ids.add(track_id)
                    unique_detections.append((cx, cy))
            else:
                # fallback if no tracking
                cx, cy = item
                unique_detections.append((cx, cy))

        # Step 1: Count per node
        zone_counts = count_people_per_zone(unique_detections)

        print("\n📊 Zone Counts:", zone_counts)

        # Step 2: Graph
        x, edge_index, nodes, node_features = get_temple_graph(zone_counts)

        # Step 3: Prediction
        pred = model(x, edge_index)

        print("\n🔮 Predictions:\n")

        for i, node in enumerate(nodes):
            predicted = int(pred[i].item())
            capacity = node_features[node][1]

            risk = get_risk(predicted, capacity)
            alert = check_alert(predicted, capacity)

            print(f"{node} → {predicted} | {risk} | {alert}")


if __name__ == "__main__":
    main()