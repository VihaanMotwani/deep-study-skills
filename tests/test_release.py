import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"
PLUGIN_ROOT = REPO_ROOT / "plugins" / "deep-study"
MANIFEST_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
EXPECTED_SKILLS = {
    "guided-tutor",
    "study-companion",
    "teach-back-student",
}


class DeepStudyReleaseTests(unittest.TestCase):
    def test_marketplace_resolves_to_the_deep_study_plugin(self) -> None:
        marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))

        self.assertEqual(marketplace["name"], "deep-study")
        self.assertEqual(marketplace["interface"]["displayName"], "Deep Study")
        self.assertEqual(len(marketplace["plugins"]), 1)

        entry = marketplace["plugins"][0]
        self.assertEqual(entry["name"], "deep-study")
        self.assertEqual(entry["source"], {
            "source": "local",
            "path": "./plugins/deep-study",
        })
        self.assertEqual(entry["policy"], {
            "installation": "AVAILABLE",
            "authentication": "ON_INSTALL",
        })

        resolved_plugin = REPO_ROOT / entry["source"]["path"]
        self.assertEqual(resolved_plugin.resolve(), PLUGIN_ROOT.resolve())

        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "deep-study")
        self.assertEqual(PLUGIN_ROOT.name, manifest["name"])
        self.assertRegex(manifest["version"], re.compile(r"^\d+\.\d+\.\d+$"))
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertEqual(manifest["mcpServers"], "./.mcp.json")

    def test_plugin_exposes_exactly_three_complete_learning_skills(self) -> None:
        skills_root = PLUGIN_ROOT / "skills"
        installed_skills = {
            path.name
            for path in skills_root.iterdir()
            if path.is_dir()
        }
        self.assertEqual(installed_skills, EXPECTED_SKILLS)

        for skill_name in sorted(EXPECTED_SKILLS):
            with self.subTest(skill=skill_name):
                skill_root = skills_root / skill_name
                skill_text = (skill_root / "SKILL.md").read_text(encoding="utf-8")

                self.assertTrue(skill_text.startswith("---\n"))
                self.assertIn(f"\nname: {skill_name}\n", skill_text)
                self.assertRegex(skill_text, r"\ndescription: .+\n")
                frontmatter = skill_text.split("---", 2)[1]
                frontmatter_keys = {
                    line.split(":", 1)[0]
                    for line in frontmatter.splitlines()
                    if line and not line.startswith((" ", "\t")) and ":" in line
                }
                self.assertEqual(frontmatter_keys, {"name", "description"})
                self.assertIn(
                    "[references/research.md](references/research.md)",
                    skill_text,
                )
                self.assertTrue((skill_root / "references" / "research.md").is_file())
                self.assertTrue((skill_root / "agents" / "openai.yaml").is_file())

    def test_live_whiteboard_is_optional_and_has_a_conversational_fallback(self) -> None:
        mcp_config = json.loads(
            (PLUGIN_ROOT / ".mcp.json").read_text(encoding="utf-8")
        )
        self.assertEqual(mcp_config, {
            "mcpServers": {
                "deep-study-whiteboard": {
                    "command": "npx",
                    "args": ["-y", "mcp-excalidraw-server@1.1.0"],
                },
            },
        })

        for skill_name in sorted(EXPECTED_SKILLS):
            with self.subTest(skill=skill_name):
                skill_text = (
                    PLUGIN_ROOT / "skills" / skill_name / "SKILL.md"
                ).read_text(encoding="utf-8")
                self.assertRegex(
                    skill_text,
                    r"If (?:a|the) live canvas cannot start,[^.]+"
                    r"offer a static [^.]+\.",
                )

    def test_public_release_contains_curated_docs_evidence_and_examples(self) -> None:
        required_files = {
            "README.md",
            "RESEARCH.md",
            "EVALUATION.md",
            "LICENSE",
            "THIRD_PARTY_NOTICES.md",
            "evals/guided-tutor/evals.json",
            "evals/study-companion/evals.json",
            "evals/teach-back-student/evals.json",
            "examples/whiteboards/guided-tutor.excalidraw",
            "examples/whiteboards/guided-tutor.png",
            "examples/whiteboards/study-companion.excalidraw",
            "examples/whiteboards/study-companion.png",
            "examples/whiteboards/teach-back-student.excalidraw",
            "examples/whiteboards/teach-back-student.png",
        }
        for relative_path in sorted(required_files):
            with self.subTest(path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())

        readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
        for required_text in (
            "# Deep Study",
            "Guided Tutor",
            "Study Companion",
            "Teach-Back Student",
            "codex plugin marketplace add VihaanMotwani/deep-study-skills",
            "codex plugin add deep-study@deep-study",
            "plugins/deep-study/skills/guided-tutor",
            "plugins/deep-study/skills/study-companion",
            "plugins/deep-study/skills/teach-back-student",
            "Node.js 18",
        ):
            with self.subTest(readme_text=required_text):
                self.assertIn(required_text, readme)

        evaluation = (REPO_ROOT / "EVALUATION.md").read_text(encoding="utf-8")
        self.assertIn("17/17", evaluation)
        self.assertIn("acceptance tests", evaluation.lower())
        self.assertIn("not causal", evaluation.lower())

        notices = (REPO_ROOT / "THIRD_PARTY_NOTICES.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("mcp-excalidraw-server", notices)
        self.assertIn("Copyright (c) 2024 MCP Excalidraw Server", notices)
        self.assertIn("https://github.com/yctimlin/mcp_excalidraw", notices)

        forbidden_paths = [
            path
            for path in REPO_ROOT.rglob("*")
            if (
                path.name == ".DS_Store"
                or path.suffix == ".html"
                or path.name.endswith("-workspace")
                or path.name.startswith("iteration-")
            )
        ]
        self.assertEqual(forbidden_paths, [])

    def test_plugin_manifest_has_public_deep_study_metadata(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

        self.assertEqual(manifest["version"], "0.1.0")
        self.assertEqual(
            manifest["description"],
            "Research-backed AI tutoring, study companionship, and teach-back.",
        )
        self.assertEqual(manifest["author"], {
            "name": "Vihaan Motwani",
            "url": "https://github.com/VihaanMotwani",
        })
        self.assertEqual(
            manifest["homepage"],
            "https://github.com/VihaanMotwani/deep-study-skills#readme",
        )
        self.assertEqual(
            manifest["repository"],
            "https://github.com/VihaanMotwani/deep-study-skills",
        )
        self.assertEqual(manifest["license"], "MIT")
        self.assertEqual(manifest["skills"], "./skills/")
        self.assertEqual(manifest["mcpServers"], "./.mcp.json")
        self.assertTrue({
            "learning",
            "tutoring",
            "study",
            "teach-back",
            "active-learning",
            "whiteboard",
        }.issubset(set(manifest["keywords"])))

        interface = manifest["interface"]
        self.assertEqual(interface["displayName"], "Deep Study")
        self.assertEqual(interface["developerName"], "Vihaan Motwani")
        self.assertEqual(interface["category"], "Education")
        self.assertEqual(interface["capabilities"], ["Interactive", "Write"])
        self.assertEqual(len(interface["defaultPrompt"]), 3)
        self.assertTrue(all(
            isinstance(prompt, str) and 10 <= len(prompt) <= 128
            for prompt in interface["defaultPrompt"]
        ))
        self.assertEqual(interface["brandColor"], "#5457D5")
        self.assertEqual(interface["composerIcon"], "./assets/icon.svg")
        self.assertEqual(interface["logo"], "./assets/icon.svg")

        icon = (PLUGIN_ROOT / "assets" / "icon.svg").read_text(encoding="utf-8")
        self.assertIn("<title>Deep Study</title>", icon)
        self.assertIn("<desc>", icon)

    def test_curated_eval_input_files_resolve_inside_the_repository(self) -> None:
        for eval_path in sorted((REPO_ROOT / "evals").glob("*/evals.json")):
            payload = json.loads(eval_path.read_text(encoding="utf-8"))
            for evaluation in payload["evals"]:
                for relative_input in evaluation.get("files", []):
                    with self.subTest(
                        eval_file=eval_path.relative_to(REPO_ROOT).as_posix(),
                        eval_id=evaluation["id"],
                        input=relative_input,
                    ):
                        resolved_input = (eval_path.parent / relative_input).resolve()
                        self.assertTrue(resolved_input.is_relative_to(REPO_ROOT))
                        self.assertTrue(resolved_input.is_file())


if __name__ == "__main__":
    unittest.main()
