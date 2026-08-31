from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "inception" / "SKILL.md"
OPENAI_YAML = ROOT / "skills" / "inception" / "agents" / "openai.yaml"
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"


def skill_description() -> str:
    text = SKILL.read_text(encoding="utf-8")
    match = re.search(r"\A---\n.*?^description:\s*(.+)$.*?^---$", text, re.MULTILINE | re.DOTALL)
    if match is None:
        raise AssertionError("SKILL.md frontmatter description was not found")
    return match.group(1).strip()


def quoted_yaml_value(text: str, key: str) -> str:
    match = re.search(rf'^\s*{re.escape(key)}:\s*"([^"]*)"\s*$', text, re.MULTILINE)
    if match is None:
        raise AssertionError(f"{key} was not found as a quoted YAML scalar")
    return match.group(1)


class SkillContractTests(unittest.TestCase):
    def test_description_frontloads_real_user_triggers(self) -> None:
        description = skill_description().lower()

        self.assertTrue(description.startswith("use when"))
        for trigger in ("less ai-like", "less generic", "less templated"):
            self.assertIn(trigger, description)
        self.assertNotIn("creating", description)

    def test_skill_routes_between_quick_and_deep_review(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        self.assertIn("## Quick Review", text)
        self.assertIn("## Deep Audit", text)
        self.assertIn("Default to Quick Review", text)

    def test_quick_review_uses_a_soft_focus_not_a_finding_cap(self) -> None:
        text = SKILL.read_text(encoding="utf-8")

        self.assertIn("usually one to three", text)
        self.assertIn("no hard maximum", text)
        self.assertNotIn("at most three", text)
        self.assertIn("Never suppress a material finding", text)
        self.assertIn("Do not select Deep Audit based on candidate count alone", text)

    def test_openai_interface_leads_with_outcome_not_internal_mechanics(self) -> None:
        text = OPENAI_YAML.read_text(encoding="utf-8")
        short_description = quoted_yaml_value(text, "short_description").lower()
        default_prompt = quoted_yaml_value(text, "default_prompt").lower()

        self.assertIn("ai-like", short_description)
        self.assertIn("intent", short_description)
        self.assertIn("ai-like", default_prompt)
        self.assertIn("intent", default_prompt)
        self.assertIn("most important", default_prompt)
        for internal_term in ("decision ledger", "independent reviewer"):
            self.assertNotIn(internal_term, default_prompt)

    def test_plugin_interface_matches_the_same_first_run_promise(self) -> None:
        payload = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
        interface = payload["interface"]
        short_description = interface["shortDescription"].lower()
        default_prompt = " ".join(interface["defaultPrompt"]).lower()

        self.assertIn("ai-like", short_description)
        self.assertIn("intent", short_description)
        self.assertIn("ai-like", default_prompt)
        self.assertIn("intent", default_prompt)
        self.assertIn("most important", default_prompt)
        for internal_term in ("decision ledger", "independent reviewer"):
            self.assertNotIn(internal_term, default_prompt)


if __name__ == "__main__":
    unittest.main()
