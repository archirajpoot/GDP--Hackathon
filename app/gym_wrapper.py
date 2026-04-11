# ============================================================
# SafetyGuard X — Gymnasium Wrapper
# Standard Gymnasium interface for RL training with SB3.
# ============================================================

import gymnasium as gym
from gymnasium import spaces
import numpy as np
from typing import Dict, Any, Tuple

from app.env import env_reset, env_step
from app.models import AgentAction

class SafetyForgeEnv(gym.Env):
    """
    Standard Gymnasium environment wrapping the SafetyGuard X logic.
    Mapped for RL training (Stable-Baselines3 compatible).
    """
    metadata = {"render_modes": ["human"]}

    def __init__(self, task_id: str = "expert"):
        super().__init__()
        self.task_id = task_id
        
        # Action Space: 5 discrete decisions
        # 0: allow, 1: block, 2: modify, 3: escalate, 4: clarify
        self.action_space = spaces.Discrete(5)
        self.action_map = {
            0: "allow",
            1: "block",
            2: "modify",
            3: "escalate",
            4: "clarify"
        }

        # Observation Space: Simple feature vector
        # [turn_num, risk_level, adversary_pressure, flags(8)]
        # Plus a simplified text feature placeholder (for v3.0)
        self.observation_space = spaces.Box(
            low=0, high=1, shape=(11,), dtype=np.float32
        )
        
        self.session_id = None

    def _get_obs(self, obs_model) -> np.ndarray:
        """Translates the Pydantic Observation model to a numerical vector."""
        # Normalize features to [0, 1]
        turn = obs_model.turn_number / obs_model.max_turns
        risk = obs_model.risk_level / 5.0
        pressure = obs_model.context.get("adversary_pressure", 0) / 5.0
        
        flags = obs_model.flags
        f_vec = [
            float(flags.escalation_detected),
            float(flags.policy_conflict),
            float(flags.encoded_detected),
            float(flags.emotional_manip),
            float(flags.roleplay_attempt),
            float(flags.late_escalation),
            float(flags.over_blocking),
            float(flags.missed_escalation)
        ]
        
        return np.array([turn, risk, pressure] + f_vec, dtype=np.float32)

    def reset(self, seed=None, options=None) -> Tuple[np.ndarray, Dict[str, Any]]:
        super().reset(seed=seed)
        
        # Reset the internal environment
        # Randomize scenario_index for better training variety
        scenario_idx = np.random.randint(0, 3) 
        reset_result = env_reset(self.task_id, scenario_idx)
        self.session_id = reset_result.session_id
        
        obs = self._get_obs(reset_result.observation)
        info = {"session_id": self.session_id}
        
        return obs, info

    def step(self, action_idx: int) -> Tuple[np.ndarray, float, bool, bool, Dict[str, Any]]:
        decision = self.action_map[action_idx]
        
        action = AgentAction(
            decision=decision,
            reason="Gym RL Agent Decision",
            confidence=0.9
        )
        
        step_result = env_step(self.session_id, action)
        
        obs = self._get_obs(step_result.observation)
        reward = step_result.reward.score
        terminated = step_result.done
        truncated = False # We manage time limits via max_turns internally
        
        info = step_result.info
        info["feedback"] = step_result.reward.feedback
        
        return obs, reward, terminated, truncated, info

    def render(self):
        # We handle rendering in the web dashboard
        pass
