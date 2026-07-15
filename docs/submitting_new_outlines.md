# How to Submit New Outlines to GLIMS

## Overview

This document is a guide to submitting new glacier outlines to the
GLIMS Glacier Database.  The GLIMS Glacier Database is a multitemporal
geospatial relational database containing glacier outlines and other
features related to mapping glacier cover.  The databse also contains
information about who created the outlines, the imagery or maps used
to digitize the outlines, and the methods used for mapping.  The
databse also tracks extinct glaciers.

A basic submission consists or one or more glacier outlines for a
region, information obout the people who mapped the outlines and the
imagery used for this mapping.

We use GitHub to track submissions.  To submit new glacier outlines to
the GLIMS Glacier Database create a [New Submission
Issue](https://github.com/glims-nsidc/glims-submissions/issues) and
filling out the New Submission form.

1. Navigate to the Issues tab in the glims-submissions GitHub Repo[^1]
2. Click the blue "New Issue" buttom.  _Add image_
3. Select "New Submission" _Add image_
4. Fill out the form.  See [Submission Metadata](#submission-metadata) for more information.
5. Upload glacier outlines

We describe the required information and file formats in the following sections.

## Required Information

### Submission Metadata

#### Submission Title

The submission title helps us track the submission.  We suggest a
title that includes the name of the submitter and the name of the
region being mapped.

For example, "Agassiz, Glacier outlines of Switzerland"

#### Geographic Region

The original GLIMS projects organized the mapping effort through
Regional Centers.  GLIMS still uses Regional Center IDs.  For your
submission please use the Regional Cneter ID that covers the outlines
you are submitting.  A list of Regional Center IDs can be found on the
[GLIMS Regional
Centers](https://www.glims.org/maps/nsidc_rc_table_public.html) page.

We also require the common name of the Geographic Region containing
the glacier outlines.  For country inventories please use the country
name (is there an ISO list). For multi-national regions, please use
the commonly accepted name for this region, for example North America,
European Alps, Himalaya, High Mountain Asia. For smaller regions,
please give the state, mountain range or other commonly recognized
term.

#### Personel

The person making the submission is the _submitter_.  Other people who
helped map glacier outlines are _analysts_.  We would like the name,
institution and an email for the _submitter_ and any _analyst_.  This
allows GLIMS to give credit to the people mapping glaciers and also
provides a contact if users of this information have questions about
the outlines.

#### Files

Please provide a description of the contents of all files you are
submitting.  See [Accepted File Formats]() for more information about
the format and structure of files.

#### Description of Analysis Methods

Please provide the date on which the analysis was performed.  Often
analyses take a while to complete.  A date to the closest month is OK.
For example, if mapping was done in October 2026, enter 2026-10-01.

Use the form the indicate any image processing that was performed,
e.g. image transformations, radiometric corrections, use of band
ratios or thresholds.

A brief description of the mapping method is also requested.  For
example, **Manual digitizing of band ratios of Sentinel-2 images**.
If an automated or semi-automated mapping procedure was used please
indicate if manual corrections were made and what percentage of
outlines were manually corrected.

#### Embargo Period

To encourage timely submission of outlines, glacier outlines submitted
to GLIMS can be embargoed for a period of time.  The length of this
time period is usually 6 months to allow analysts to prepare and
submit journal articles.


### Glacier Outlines and other glacier features

#### Features in the GLIMS Glacier Database

The majority of features in the GLIMS Glacier Database are glacier
outlines.  However, the database also contains the outline of debris
cover on glaciers; supraglacial and proglacial lakes; center lines of
glaciers; and transient snow lines.  Glacier outlines are the only
**required** features.

#### Accepted file formats

Glacier features can be submitted as ESRI Shapefiles or GeoJSON.  Most
submissions use ESRI Shapefile.

#### Feature Geometry

A glacier outline, debris cover, supraglacial lake or proglacial lake
can be either a Polygon or MultiPolygon.  Center lines and transient
snowlines should be LineStrings or MultiLineStrings

Each type of glacier feature is mapped as a seprate vector entity.

Glacier outline features should represent Nunataks[^2] as _holes_.
Exposed ice within areas of debris cover and proglacial lakes, and
islands in supraglacial lakes may also be represented as _holes_.

Fragmented glaciers can be mapped as MultiPolygons, where each
fragment is a polygon in the MultiPolygon collection.  Alternatively,
fragments can be mapped as separate Polygons.  If fragments are mapped
as separate Polygon features, all of the fragments of the same
glacier must have the same id (see [feature attributes]())[^3].  

Glacier outlines, debris cover, supraglacial lakes and proglacial lake features may be combined in a single shapefile.  If multiple feature types are included in the same shapefile, each feature must have a `category` attribute.  See [Attributes](attributes).

#### Attributes

| Attribute Name | Description | Data Type | Example |
|----|------------|---|-----|
| `name` | Glacier Name | string | `"Unteraargletscher"` |
| `local_id` | ID assigned to glacier by analyst or part of regional inventory | string | `"0001"` |
| WGMS glacier ID | ID assigned by World Glacier Monitoring Service | string | |
| Image ID | ID for image assigned by image provider | string | |
| Map ID | ID of map assigned by map publisher.  E.g. Sheet number | string | |
| Instrument Name | Recognized name of instrument. | string | "Sentinel-2", "SuperDove" |
| Acquisition Date | Date of image acquisition in ISO 8640 format | string | 2026-08-13 |
| Analyst Name | Name of analyst who created outline | string | "Agassiz, Louis" |
| `category` | Category of feature | string | "glacier_bound" |


Accepted `category` values.

| `category` value | Description | Feature Types |
|----------|--------------|---------------------|
| "glac_bound" | Glacier boundary | Polygon or MultiPolygon with holes |
| "centerline" | Glacier centerline | LineString or MultiLineString |
| "snow_line" | Location of snow line | LineString or MultiLineString |
| "pro_lake" | Proglacial Lakes | Polygon or MultiPolygon with holes |
| "supra_lake" | Supraglacial Lake outline | Polygon or MultiPolygon with holes |
| "debris_cov" | Debris covered glacier ice | Polygon or MultiPolygon with holes |

[^1]: You will need a GitHub account.  You can register for a free GitHub account [here](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).

[^2]: A Nunatak is a mountain, or any exposed ground or bedrock, that projects from and is surrounded by glacier ice.

[^3]: A glacier id can be an arbitrary identifier assigned by an analyst or an identifier assigned as part of a local glacier inventory.  GLIMS assigns GLIMS Glacier IDs to glaciers.  However, the GLIMS glacier database stores local identifiers.