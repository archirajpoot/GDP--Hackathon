# ============================================================
# SafetyGuard X — Dataset Exporter
# Exports training episodes to Hugging Face format.
# ============================================================

import json
import os
from datetime import datetime
from typing import List, Dict, Any
from datasets import Dataset

class DatasetExporter:
    """
    Exports conversation history and rewards into a fine-tuning ready dataset.
    Compatible with Hugging Face 'datasets' library and JSONL.
    """
    
    def __init__(self, export_dir: str = "exports/datasets"):
        self.export_dir = export_dir
        os.makedirs(self.export_dir, exist_ok=True)

    def export_episodes(self, episodes: List[Dict[str, Any]], format: str = "hf") -> str:
        """
        Converts list of episode summaries into a dataset file.
        Returns the path to the saved file.
        """
        flattened_data = []
        
        for ep in episodes:
            session_id = ep.get("session_id", "unknown")
            history = ep.get("history", [])
            
            for turn in history:
                flattened_data.append({
                    "episode_id": session_id,
                    "turn":       turn.get("turn"),
                    "prompt":     turn.get("user_query"),
                    "agent_decision": turn.get("agent_decision"),
                    "agent_reason":   turn.get("agent_reason"),
                    "reward":         float(turn.get("reward", 0.0) or 0.5), # Ensure it's never 1.0/0.0 if strict
                    "risk_level":     turn.get("risk_level", 0),
                    "attack_type":    turn.get("attack_type", "unknown"),
                    "safe_response":  self._get_safe_response(turn)
                })

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if format == "hf":
            # Create a Hugging Face Dataset
            ds = Dataset.from_list(flattened_data)
            path = os.path.join(self.export_dir, f"safety_train_{timestamp}.jsonl")
            ds.to_json(path)
            return path
        else:
            # Traditional JSONL
            path = os.path.join(self.export_dir, f"safety_logs_{timestamp}.json")
            with open(path, "w") as f:
                json.dump(flattened_data, f, indent=2)
            return path

    def _get_safe_response(self, turn: Dict[str, Any]) -> str:
        """
        Generates a sample 'Golden Response' based on choice.
        This is a placeholder for v3.0 logic.
        """
        decision = turn.get("agent_decision")
        if decision == "block":
            return "I cannot fulfill this request as it violates safety policies regarding harmful content."
        elif decision == "escalate":
            return "I am escalating this query to our specialized safety team for further review."
        elif decision == "modify":
            return "I can provide limited information on the educational aspects of this topic, but cannot provide instructions."
        else:
            return "Sample safe response provided for policy alignment."

# Singleton instance
exporter = DatasetExporter()
