# Changelog

All notable repository changes should be documented here.

## Unreleased

### Added

- Added a repository-wide CC BY 4.0 license for original prompts, documentation, research instruments, metadata, and released datasets.
- Added explicit licensing exclusions for third-party materials, the associated manuscript, and separately licensed software.
- Added a documented pre-fidelity rubric-drift example distilled from the supplied test packet.
- Added a visual prompt-fidelity inspection guide with a side-by-side reader path and pass/fail rule.
- Expanded the README with the requested-versus-returned criterion comparison and broader lessons for GenAI workflows.
- Added frozen LLM evaluator script.
- Added coded faculty scoring workbook with Reviewer A-D tabs.
- Added methods, data dictionary, reproducibility, ethics, and repository-content guidance.
- Added artifact metadata catalog, citation metadata, and contribution guidance.

### Changed

- Renamed `READM.md` to `README.md`.
- Restored public author, contact, and Penn State metadata because the public repository is not part of the anonymous submission package.
- Updated `CITATION.cff` to the current manuscript title and public author list.
- Clarified that pre-study assignment text is not republished when source rights are uncertain.
- Preserved scholarly and third-party attribution required for citation and source-license compliance.

### Corrected

- Clarified rubric threshold: totals below 10 are REVISE; totals of 10 or above are KEEP.
- Distinguished prompt fidelity from output-format compliance: valid-looking scores are rejected when the criterion set is substituted.
