# Submitting a Resubmission or Correction to GLIMS

## Background

Glacier outline submissions to GLIMS sometimes need to be revised after they have already been ingested into the GLIMS Glacier Database. This can happen for a number of reasons: an error is discovered in the geometry or metadata, a submitter provides updated or corrected data, or the instrument, session, or analyst information associated with a submission needs to be fixed.

The Ingest Resubmission/Correction issue form gives submitters and analysts a consistent way to flag these cases so the NSIDC DAAC team can identify what changed, trace it back to the original submission, and determine the right course of action.

## Before Submitting

Before opening a resubmission, identify the submission that needs to be corrected. You will need:

* The **original submission ID** (the `Submission_Info` ID in the GLIMS database)
* The **RC ID** or region label associated with the original submission
* A link to the GitHub issue or documentation from the original submission 

If you are unsure which submission needs correcting, you can search the [GLIMS Glacier Viewer](https://www.glims.org/maps/glims). If the data you want to submit does not correspond to any existing submission, use the [new submission form](https://github.com/glims-nsidc/glims-submissions/issues) instead as this form is only for changes to data that has already been submitted.

## Required Information

For each resubmission or correction, you will need the following:

**Original submission ID(s)** — The `Submission_Info` ID, RC ID, or other identifier for the submission(s) being corrected or resubmitted.

**Link to previous submission** (optional) — The URL of the GitHub issue for the original submission, if available. This helps the analyst quickly pull up the full history of the original request. Trello link or documentation from prior emails is also acceptable here as this transition to github is still ongoing.

**Reason for resubmission** — A short categorization of why the resubmission is needed. Options include:
* Geometry/outline correction
* Metadata error (e.g. `rc_id`, `region_label`, `submitter_id`)
* Instrument/session info correction
* Analyst assignment correction
* New or corrected data from submitter
* Other (explained in the notes field)

**Scope of change** — One or more checkboxes indicating what the resubmission affects: outlines/geometry, attribute/metadata only, instrument or session info, and/or analyst assignment. This helps the analyst anticipate whether a full delete-and-reingest is required or whether the issue can be resolved with a direct SQL correction.

**Additional notes** — Any context useful for the analyst processing the request: why the correction is needed, what specifically changed, and anything unusual about the original ingest that might affect how the correction should be handled.

## How to Submit

Resubmissions and corrections are handled through the GLIMS submissions GitHub repository using an issue form.

1. Navigate to the [glims-submissions repository](https://github.com/glims-nsidc/glims-submissions/issues)
2. Click **New Issue**.
3. Select the **Glacier Ingest Resubmission/Correction** template.
4. Fill in the title with a brief description, for example: `Ingest Resubmission/Correction: Norway 2024/2025 outlines`.
5. Enter information into form fields.
8. Click **Submit new issue**.

## After Submission

Once submitted, the issue is automatically labeled `resubmission`, which triggers two automated workflows: one parses the issue into a structured JSON record for the ingest pipeline, and the other creates a corresponding Story in the DPT Jira project for tracking. An NSIDC DAAC analyst will then review the request. You may be contacted with questions before the correction is processed.

## Questions

For questions, please contact NSIDC User Services at nsidc@nsidc.org.
