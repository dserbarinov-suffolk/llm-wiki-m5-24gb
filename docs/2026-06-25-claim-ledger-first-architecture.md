# Claim-Ledger-First Architecture - Domain Design Document (DDD) (2026-06-25)

## Context & Problem

`RawSource` is one immutable source supplied to ingest.
`SourceLocator` is a portable reference to a source or source span.
`SourceHash` is a hash of source bytes or extracted source text.
`EvidenceRegistryHash` is the hash of one evidence registry artifact.
`SourceRange` is one bounded span inside a source.
`SourceRangeId` is the stable id for one source range.
`SourceOrder` is the order induced by `SourceRange` positions.
`SourceText` is the exact text in one source range.
`EvidenceRecord` is one source evidence record with text, range, locator, and hash.
`EvidenceIds` are ordered ids for evidence records.
`EvidenceRegistry` is the existing source-scoped artifact that stores source evidence records.
`ExtractedUnit` is one extracted source segment before claim or atom classification.
`ExtractedUnitDisposition` is the required accounting decision for one extracted unit.
`accepted`, `structural`, `needs-review`, `rejected`, and `non-claim` are extracted-unit disposition values.
`DispositionCount` is the count of extracted units for one `ExtractedUnitDisposition`.
`DispositionCountValue` is the count value for one `DispositionCount`.
`FeatureSignal` is one measured source-neutral property of an extracted unit.
`FeatureSignalId` is the stable id for one feature signal.
`FeatureSignalKind` is the controlled reusable category for one feature signal.
`FeatureSignalValue` is the typed measured value for one feature signal.
`FeatureSignalConfidence` is the confidence for one feature signal measurement.
`FeatureSignalPolicy` validates feature signal kinds and detector contracts.
`ExtractedUnitProfile` is the measured feature signal set for one extracted unit.
`ExtractorCapability` is one declared atom kind and evidence contract that an extractor can produce.
`ExtractorCapabilityId` is the stable id for one extractor capability.
`ActiveExtractorCapabilitySet` is the ordered extractor capability set active for one ingest run.
`ExtractorDecisionId` is the stable id for one extractor decision.
`ExtractorDecisionStatus` is one of `candidate-produced` or `abstained`.
`ExtractorDecision` is one extractor outcome for one extracted unit and one extractor capability.
`AtomCandidateId` is the stable id for one atom candidate.
`AtomCandidatePayload` is the typed payload proposed for one technical atom.
`RankerScore` is the calibrated source-neutral score for one atom candidate or abstained extractor decision.
`RankerScoreRange` is the normalized score interval allowed by `CalibrationPolicy`.
`CalibrationBucket` is the controlled calibration band for one ranker score.
`CalibrationBucketSet` is the controlled set of calibration buckets.
`CalibrationThreshold` is the score boundary for one calibration bucket and one extractor capability.
`CalibrationThresholds` are score boundaries keyed by extractor capability id.
`CalibrationPolicy` validates `RankerScoreRange`, `CalibrationBucketSet`, and `CalibrationThresholds`.
`AbstainReasonKind` is the controlled reusable category for one abstain reason.
`AbstainReasonFields` are typed fields required by one abstain reason kind.
`EvidenceRequirement` is the typed missing evidence requirement for one abstain reason.
`AmbiguityBasis` is the typed ambiguity description for one abstain reason.
`SchemaFailure` is the typed schema validation failure for one abstain reason.
`ScoreGate` is the typed score and threshold pair for one abstain reason.
`UnsupportedModality` is the typed unsupported source modality for one abstain reason.
`AbstainReason` is the structured reason an extractor decision abstained.
`AbstainReasonPolicy` validates abstain reason kinds and required typed fields.
`FeatureSignalIds` are ordered ids for feature signals that contributed to one atom candidate or extractor decision.
`AtomSchema` is the deterministic validation contract for one technical atom kind.
`AtomSchemaSet` is the active portable set of atom schemas for one ingest run.
`AtomValidator` is domain logic that validates atom candidates against an atom schema set.
`AtomCandidate` is one materialized technical atom candidate with evidence, payload, score, and validation status.
`ConfidencePolicy` is the deterministic policy that maps extraction signals to confidence and status.
`ExtractionConfidence` is the confidence that a ledger entry faithfully represents source text.
`ConfidenceBasis` is the structured reason for one extraction confidence value.
`ReviewReason` is the structured reason an entry requires review or was rejected.
`RawTableText` is the exact extracted table text or closest source-equivalent table representation.
`TableRow` is one ordered row in a logical table model.
`TableColumn` is one ordered column in a logical table model.
`TableCell` is one cell value with row and column coordinates.
`TableCaption` is source-derived caption text for a table.
`TableNote` is source-derived note text attached to a table.
`RawCodeText` is exact source code text including whitespace.
`LanguageTag` is the source-declared or detected programming or markup language.
`LanguageConfidence` is the confidence for a detected language tag.
`CodeFence` is the source fence marker for a code block.
`LineOrder` is the source order of lines in a code block.
`SurroundingExplanationLocator` is the source locator for nearby explanatory text.
`CodeAst` is optional deterministic parser output for code text.
`RuleText` is exact source wording for one rule atom.
`RuleForce` is the prescriptive, permissive, prohibitive, or advisory force of one rule atom.
`RuleScope` is the governed entity or context for one rule atom.
`RuleTrigger` is the source condition that activates one rule atom.
`RuleEffect` is the action, result, calculation, or constraint imposed by one rule atom.
`RuleException` is the source exception for one rule atom.
`RuleCandidateProfile` is the source-neutral feature and role profile for one rule candidate.
`RuleSchema` is the active atom schema for rule atoms.
`ProcedureText` is exact source wording for one procedure atom.
`ProcedureGoal` is the source-derived goal of one procedure atom.
`ProcedureInput` is one source-derived input for one procedure atom.
`ProcedurePrecondition` is one source-derived precondition for one procedure atom.
`ProcedureStep` is one ordered source-derived step in one procedure atom.
`ProcedureOutput` is one source-derived output for one procedure atom.
`ProcedureException` is one source-derived exception for one procedure atom.
`ExampleText` is exact source wording for one worked example atom.
`ExampleSetup` is the source-derived setup for one worked example atom.
`ExampleInput` is one source-derived input for one worked example atom.
`ExampleOperation` is one source-derived operation in one worked example atom.
`ExampleOutput` is one source-derived output for one worked example atom.
`ExampleExplanation` is source-derived explanatory text for one worked example atom.
`ReferencedAtomIds` are atom ids referenced by one technical atom.
`ParseStatus` is the parser result for one technical atom payload.
`FormulaSubtype` is the semantic category for a formula atom.
`FormulaSurfaceForm` is the source expression form for a formula atom.
`QuotationText` is exact source wording preserved because wording matters.
`SourceStatement` is one source-bounded statement that can produce multiple ledger entries.
`SourceStatementId` is the stable id for one source statement.
`DerivedEntryIds` are ledger entry ids derived from one source statement.
`StatementRelationship` is a source-local relation among entries derived from one source statement.
`SourceClaim` is one candidate factual statement from an extracted unit.
`WikiPage` is one generated markdown page in the wiki layer.
`SourceWikiPage` is one `WikiPage` for one `RawSource`.
`CrossSourceWikiPage` is one `WikiPage` that uses records from more than one `RawSource`.
`WikiPageLocator` is the portable wiki-layer locator for one wiki page.
`WikiPageMetadata` is non-body metadata for one wiki page.
`PageBody` is the visible markdown body of a wiki page.
`PageBodyHash` is the hash of one `PageBody`.
`ArtifactFormat` is the canonical serialized shape for one portable artifact.
`ArtifactFingerprint` is a hash of the domain-relevant artifact contents.
`ArtifactLocatorFingerprint` is the artifact fingerprint value stored by an artifact locator.
`PortableArtifact` is any importable persisted artifact with a deterministic id, `ArtifactFormat`, canonical ordering, and one typed artifact fingerprint field.
`PortableArtifactKind` is the controlled artifact domain type for one portable artifact.
`PortableArtifactMember` is one manifest row for one child artifact in a portable artifact set.
`PortableArtifactSetId` is the stable id for one portable artifact set manifest.
`PortableArtifactSetFingerprint` is the `ArtifactFingerprint` for canonical `PortableArtifactSet` manifest contents.
`PortableArtifactPointer` is one structured reference with target artifact id and target artifact fingerprint.
`TypedArtifactPointerAlias` is a domain-specific name that binds `PortableArtifactPointer` to one target artifact type.
`PortableArtifactSet` is the first-class manifest artifact that addresses child portable artifacts by deterministic ids and fingerprints.
`SourceCitationLabel` is a visible source title, section, page, or source range label.
`SourceCitation` is one visible source-facing citation in `PageBody`.
`ProjectionCoverageArtifact` is the portable persisted form of projection coverage for one wiki page.
`ProjectionCoverageArtifactId` is the stable id for one `ProjectionCoverageArtifact`.
`ProjectionCoverageFingerprint` is the `ArtifactFingerprint` for canonical `ProjectionCoverageArtifact` contents.
`ProjectionCoveragePointer` is a `TypedArtifactPointerAlias` for `ProjectionCoverageArtifactId` and `ProjectionCoverageFingerprint`.
`BlockedWriteDiagnosticArtifact` is the portable persisted form of one blocked authoritative wiki page write.
`BlockedWriteDiagnosticArtifactId` is the stable id for one `BlockedWriteDiagnosticArtifact`.
`BlockedWriteDiagnosticFingerprint` is the `ArtifactFingerprint` for one `BlockedWriteDiagnosticArtifact`.
`PageTextRange` is one bounded span inside `PageBody`.
`TechnicalAtom` is one preserved structured item such as a table, code block, formula, procedure, rule, or worked example.
`DomainConcept` is one source-derived concept record with source-neutral facets and evidence.
`RelationshipEntry` is one source-derived edge between concepts, events, claims, or technical atoms.
`ClaimLedger` is one source-scoped artifact that records source-derived entries before any wiki page write.
`ClaimLedgerId` is the stable id for one claim ledger.
`ClaimLedgerFingerprint` is the `ArtifactFingerprint` for one `ClaimLedgerArtifact`.
`ClaimLedgerPointer` is a `TypedArtifactPointerAlias` for `ClaimLedgerId` and `ClaimLedgerFingerprint`.
`LedgerEntry` is one source-derived claim, source note, concept, relationship, or technical atom inside a claim ledger.
`LedgerEntryId` is the stable id for one ledger entry.
`LedgerEntryKind` is the category of one ledger entry.
`LedgerEntryStatus` is the decision that controls whether one ledger entry can appear in generated prose.
`GeneratedPageClaim` is one claim asserted by generated page prose.
`SourceBackedPosition` is one `GeneratedPageClaim` backed by one `RawSource`.
`CrossSourceRelationshipKind` is one of `conflicts-with`, `agrees-with`, `qualifies`, or `supersedes`.
`CrossSourceRelationship` is one projection relation among `SourceBackedPosition` records on one `CrossSourceWikiPage`.
`CrossSourceRelationshipId` is the stable id for one `CrossSourceRelationship`.
`SourceEquivalentPayload` is rendered content that preserves source text, source structure, field labels, field order, and required whitespace.
`RenderedTechnicalAtomBlock` is one `SourceEquivalentPayload` for a table, code block, formula, procedure, rule, or worked example inside `PageBody`.
`SynthesisSection` is secondary `PageBody` prose whose `GeneratedPageClaim` units combine `LedgerEntry` records.
`SourceReviewItem` is one structured page item for one `LedgerEntry` with `LedgerEntryStatus` `needs-review`.
`SourceReviewSection` is one structured `PageBody` section for `SourceReviewItem` and `DispositionCount` records.
`ProjectionCoverageUnitKind` is one of `generated-page-claim`, `rendered-technical-atom-block`, `source-review-item`, `disposition-count`, or `cross-source-relationship`.
`ProjectionCoverageUnit` is one `GeneratedPageClaim`, `RenderedTechnicalAtomBlock`, `SourceReviewItem`, `DispositionCount`, or `CrossSourceRelationship`.
`ProjectionSourceSupportId` is the stable id for one `ProjectionSourceSupport`.
`ProjectionSourceSupport` is one support record for one `RawSource` used by one page projection.
`ProjectionSourceSupportSet` is the ordered set of `ProjectionSourceSupport` records for one page projection.
`index.md` is the wiki navigation index.
`log.md` is the chronological wiki maintenance log.
`DocumentStructure` is the authoritative extracted source organization.
`StructureNode` is one heading, chapter, section, glossary entry, index entry, reference entry, or other source structure item.
`SourceStructureSection` is one `PageBody` section derived from one `StructureNode`.
`StructureNodeIds` are ordered ids for structure nodes that contain or contextualize a ledger entry.
`DocumentStructureArtifactId` is the stable id for one document structure artifact.
`DocumentStructureFingerprint` is the `ArtifactFingerprint` for one `DocumentStructureArtifact`.
`DocumentStructureArtifact` is the portable persisted form of one document structure.
`DocumentStructurePointer` is a `TypedArtifactPointerAlias` for `DocumentStructureArtifactId` and `DocumentStructureFingerprint`.
`SourceStructureSpine` is the ordered page spine derived from `DocumentStructure` and `SourceOrder`.
`SourceProfile` is the aggregate profile derived from unit profiles and accepted ledger records.
`SourceFamily` is an optional source category derived from a source profile.
`SourceFamilyAssignment` is the scored label set derived from a source profile.
`Universal Standard` is the rule that production logic derives from source categories and never from one source particularity.
`NormalizedText` is source-close text that a page projection can cite.
`ResolutionBasis` is the evidence-backed reason for normalized text.
`Subject` is the source-derived subject of a claim-like ledger entry.
`Predicate` is the source-derived relation or action of a claim-like ledger entry.
`Object` is the source-derived object, value, or complement of a claim-like ledger entry.
`Polarity` is the affirmative or negative state of a claim-like ledger entry.
`ClaimForce` is the source-derived factual, modal, or deontic force of a claim-like ledger entry.
`ConditionScope` is the applicability shape of a claim-like ledger entry.
`ConditionText` is the source-derived condition for a conditional claim-like ledger entry.
`ExceptionText` is the source-derived exception for a claim-like ledger entry.
`TemporalScope` is the source-derived time, date, duration, sequence, or unknown value for a claim-like ledger entry.
`TemporalText` is exact source wording for temporal scope.
`TemporalKind` is the category of one temporal scope.
`NormalizedTemporalValue` is the normalized temporal value when safe.
`TemporalAnchorEntryIds` are ledger entry ids that anchor relative temporal scope.
`TemporalConfidence` is the resolution state for one temporal scope.
`SpatialScope` is the source-derived place, location, setting, or unknown value for a claim-like ledger entry.
`SpatialText` is exact source wording for spatial scope.
`SpatialKind` is the category of one spatial scope.
`NormalizedSpatialValue` is the normalized spatial value when safe.
`SpatialAnchorEntryIds` are ledger entry ids that anchor relative spatial scope.
`SpatialConfidence` is the resolution state for one spatial scope.
`ClaimRoleTags` are role labels from an extracted source claim.
`TechnicalAtomKind` is the category of one technical atom.
`TechnicalAtomId` is the stable id for one technical atom.
`InternalSupportId` is any ledger, coverage, artifact, or technical atom id used for projection support.
`ConceptFacets` are source-neutral facets for concept and event entries.
`RelationshipKind` is the typed predicate for one relationship entry.
`RelatedEntryIds` are ledger entry ids that provide local context.
`EntryFingerprint` is a hash of the domain-relevant contents of one ledger entry.
`PayloadFingerprint` is a hash of the domain-relevant contents of one technical atom payload.
`HeadingTextFingerprint` is a hash of normalized heading or structure text.
`Entries` are the ordered ledger entries in one claim ledger artifact.
`RejectedCandidates` are rejected atom or claim candidates retained for completeness and future review.
`ExtractorDecisions` are ordered extractor decision records retained for audit.
`CanonicalOrder` is the deterministic array and object ordering for portable artifact serialization.
`QualityReportScope` is one of `ledger-build`, `page-projection`, `blocked-write`, or `cross-source-projection`.
`QualityReport` is the domain category for quality report records scoped by `QualityReportScope`.
`ClaimLedgerArtifact` is the portable persisted form of one claim ledger.
`LedgerProjectionPlan` is the selected ledger entry coverage for one `WikiPage`.
`SelectedLedgerEntryIds` are ordered ledger entry ids selected to support one projection coverage entry.
`ProjectionCoverageEntryId` is the stable id for one projection coverage entry.
`RelatedProjectionCoverageEntryIds` are ordered projection coverage entry ids related by one `CrossSourceRelationship`.
`ProjectionCoverageEntry` is one mapping from one `ProjectionCoverageUnit` to its required support fields.
`ProjectionCoverage` is the ordered set of `ProjectionCoverageEntry` records for one `WikiPage`.
`LedgerQualityReport` is the deterministic report for one `QualityReportScope`.
`LedgerQualityReportArtifact` is the portable persisted form of one `LedgerQualityReport`.
`LedgerQualityReportArtifactId` is the stable id for one `LedgerQualityReportArtifact`.
`LedgerQualityReportFingerprint` is the `ArtifactFingerprint` for canonical `LedgerQualityReport` contents.
`LedgerQualityReportPointer` is a `TypedArtifactPointerAlias` for `LedgerQualityReportArtifactId` and `LedgerQualityReportFingerprint`.
`QualityFindingSeverity` is one of `blocking`, `warning`, or `info`.
`QualityFindingSeverityOrder` is `blocking`, then `warning`, then `info`.
`QualityFindingReason` is one controlled source-neutral reason kind for a quality report record.
`QualityFindingReasonTaxonomy` is the controlled set of `QualityFindingReason` values.
`QualityCheckId` is the stable id for one exact quality check.
`QualityCheckDefinition` is one catalog record for one exact quality check.
`QualityCheckCatalog` is the controlled set of `QualityCheckDefinition` records.
`QualityCheckCatalogArtifact` is the portable persisted form of one `QualityCheckCatalog`.
`QualityCheckCatalogArtifactId` is the stable id for one `QualityCheckCatalogArtifact`.
`QualityCheckCatalogFingerprint` is the `ArtifactFingerprint` for canonical `QualityCheckCatalog`, `ReasonApplicabilityPolicy`, and `QualityFindingSeverityPolicy` contents.
`QualityCheckCatalogPointer` is a `TypedArtifactPointerAlias` for `QualityCheckCatalogArtifactId` and `QualityCheckCatalogFingerprint`.
`QualityFindingSubjectKind` is one controlled domain object kind named by a quality report record.
`QualityFindingSubjectId` is the stable id for the domain object named by a quality report record.
`QualityFindingSubjectField` is one domain field name or `whole-object`.
`QualityFindingSubject` is one structured subject with `QualityFindingSubjectKind`, `QualityFindingSubjectId`, and `QualityFindingSubjectField`.
`QualityFindingLocatorKind` is one controlled portable locator kind named by a quality report record.
`QualityFindingLocator` is one structured locator with `QualityFindingLocatorKind` and the required locator fields.
`AllowedQualityReportScopes` are the `QualityReportScope` values allowed for one `QualityFindingReason`.
`AllowedQualityFindingSubjectKinds` are the `QualityFindingSubjectKind` values allowed for one `QualityFindingReason`.
`ReasonApplicabilityPolicy` maps each `QualityFindingReason` to `AllowedQualityReportScopes` and `AllowedQualityFindingSubjectKinds`.
`QualityFinding` is one deterministic report record with `QualityCheckId`, `QualityReportScope`, `QualityFindingSeverity`, `QualityFindingReason`, `QualityFindingSubject`, and `QualityFindingLocator`.
`QualityFindingSeverityPolicy` is the deterministic policy that maps each `QualityFindingReason` to one `QualityFindingSeverity`.
`PageWriteDecision` is one of `block-authoritative-write`, `write-with-review-work`, or `write-authoritative-page`.
`ReviewWorkItem` is one review item derived from one `QualityFinding` with `QualityFindingSeverity` `warning`.
`WriteBoundary` is the domain boundary that maps `LedgerQualityReport` to `PageWriteDecision`.
`ClaimLedgerBuilder` is the domain service that creates claim ledger records from source artifacts.
`LedgerProjectionPlanner` is the domain service that selects usable ledger entries for one `WikiPage`.
`WikiPageRenderer` is the adapter service that renders one `WikiPage` from a ledger projection plan.
`Port` is a boundary contract that the domain module calls or receives.
`Adapter` is infrastructure code that satisfies a port.
`SourceArtifactInputPort` is the port that supplies source artifact records, unit profiles, extractor decisions, and atom candidates.
`SchemaInputPort` is the port that supplies atom schema set, active extractor capability set, feature signal policy, abstain reason policy, `CalibrationPolicy`, confidence policy, and page contracts.
`LedgerOutputPort` is the port that receives claim ledger records from domain logic.
`ProjectionInputPort` is the port that supplies ledger and page contract records to domain logic.
`ProjectionOutputPort` is the port that receives ledger projection records from domain logic.
`CoverageOutputPort` is the port that receives `ProjectionCoverageArtifact` records from page rendering.
`DiagnosticOutputPort` is the port that receives `BlockedWriteDiagnosticArtifact` records from domain logic.
`QualityReportOutputPort` is the port that receives `LedgerQualityReport` records from domain logic.
`SourceExtractionAdapter` is the adapter that reads raw files and creates source artifact records.
`ModelAdapter` is the adapter that calls an LLM and returns structured artifact records.
`SchemaAdapter` is the adapter that reads atom schema set, active extractor capability set, feature signal policy, abstain reason policy, `CalibrationPolicy`, confidence policy, and page body contracts.
`LedgerStoreAdapter` is the adapter that persists claim ledger artifacts.
`QualityReportStoreAdapter` is the adapter that persists quality report artifacts.
`DocumentStructureStoreAdapter` is the adapter that persists document structure artifacts.
`DiagnosticStoreAdapter` is the adapter that persists `BlockedWriteDiagnosticArtifact` records.
`ArtifactManifestBuilder` is pure domain logic that builds `PortableArtifactSet` from portable artifact descriptors.
`ArtifactManifestOutputPort` is the port that receives `PortableArtifactSet` records from domain logic.
`ArtifactManifestStoreAdapter` is the adapter that persists `PortableArtifactSet` records.
`WikiStoreAdapter` is the adapter that writes generated wiki page markdown.
`LogAdapter` is the adapter that updates wiki navigation and maintenance logs.
`domain` is the pure package namespace for claim ledger domain code.
`DomainModule` is the pure `domain` module that owns claim ledger domain objects and domain logic.

Current ingest creates source-summary pages from selected `SourceClaim` records.
Those pages can read like rough summaries when a model resolves fragments, broadens claims, or drops technical details.
This design makes `ClaimLedger` the first generated source-derived artifact.
Source pages become projections of `ClaimLedger`, not independent summaries.

## Goals

- Add `ClaimLedger` as the primary source-derived artifact for one `RawSource`.
- Preserve source-close claims before any generated prose page exists.
- Preserve `TechnicalAtom` records before any summary writes them.
- Preserve tables in their entirety as source-equivalent table payloads.
- Preserve code blocks in their entirety as source-equivalent code payloads.
- Preserve mathematical formulas as source-equivalent formula payloads.
- Preserve `DocumentStructureArtifact` as a sibling artifact to `ClaimLedgerArtifact`.
- Account for every `ExtractedUnit` with one disposition.
- Profile each `ExtractedUnit` before selecting extraction strategies.
- Rank extractor capabilities from source-neutral feature signals.
- Record one `ExtractorDecision` for each extracted unit and active extractor capability.
- Validate atom candidates against the active atom schema set.
- Derive `SourceProfile` from accepted atoms, concepts, relationships, and unit profiles.
- Generate `WikiPage` content from `LedgerProjectionPlan`.
- Keep `ProjectionCoverage` so each `ProjectionCoverageUnit` traces to `ProjectionSourceSupportSet`.
- Mark fragmentary or ambiguous entries as review work instead of prose assertions.
- Evaluate history, coding, and rules-reference sources as emergent profile acceptance targets.
- Track domain concepts and relationships as ledger records.
- Keep `ClaimLedger` portable between llm-wiki implementations.
- Keep `SourceFamilyAssignment` derived from source profiles under the `Universal Standard`.

## Proposed Architecture

### Design Shape

The design uses ports-and-adapters architecture.
The `DomainModule` contains the domain objects and domain logic.
The `DomainModule` does not read files, write files, call models, call databases, or inspect process state.
The `DomainModule` receives typed input records and returns typed output records.
Adapters perform all I/O before or after domain logic runs.

```
+-------------------+        +-------------------+
| Source Adapters   |------->|                   |
+-------------------+        |                   |
                             |                   |
+-------------------+        |                   |        +-------------------+
| Model Adapters    |------->|   DomainModule    |------->| Storage Adapters  |
+-------------------+        |                   |        +-------------------+
                             |                   |
+-------------------+        |                   |        +-------------------+
| Schema Adapters   |------->|                   |------->| Wiki Adapters     |
+-------------------+        +-------------------+        +-------------------+
```

The arrows carry data contracts.
The arrows do not carry infrastructure dependencies into the `DomainModule`.

### Architecture Invariants

- `RawSource` is the final authority.
- `DocumentStructureArtifact` is a sibling artifact to `ClaimLedgerArtifact`.
- `DocumentStructureArtifact` stores source organization, not subject-matter claims.
- Normal ingest always produces `DocumentStructureArtifact`.
- Structurally flat sources get a root-only `DocumentStructureArtifact`.
- `ClaimLedgerArtifact` stores extracted subject-matter records.
- `ClaimLedgerArtifact` uses one canonical JSON document per source.
- `ClaimLedgerArtifact` references `DocumentStructureArtifact` with `DocumentStructurePointer`.
- `ClaimLedgerArtifact` does not embed full `DocumentStructure`.
- Portable artifact ids are deterministic.
- `WikiPage` is authoritative only as a projection of `ProjectionSourceSupportSet`.
- `ClaimLedger` remains portable between llm-wiki implementations.
- `ClaimLedger` uses source locators and evidence ids, not local file paths as authority.
- `ClaimLedger` stores domain records, not model prompts or model transcripts.
- `ClaimLedgerArtifact` stores source-neutral ranker fields on atom candidates and extractor decisions only.
- `ClaimLedgerArtifact` does not store raw ranker internals.
- `DomainModule` has no I/O and no side effects.
- `DomainModule` owns domain objects and domain rules.
- `DomainModule` owns technical atom domain objects and atom validation behavior.
- `AtomSchemaSet` declares required fields for each technical atom kind.
- `SchemaInputPort` supplies the active `AtomSchemaSet`.
- `SchemaInputPort` supplies the active `ActiveExtractorCapabilitySet`.
- `SchemaInputPort` supplies the active `FeatureSignalPolicy`.
- `SchemaInputPort` supplies the active `AbstainReasonPolicy`.
- `SchemaInputPort` supplies the active `CalibrationPolicy`.
- `ActiveExtractorCapabilitySet` uses canonical order.
- `RankerScore` uses `RankerScoreRange`.
- `CalibrationBucket` uses a controlled vocabulary.
- `CalibrationPolicy` defines `CalibrationThresholds` per active extractor capability.
- `CalibrationPolicy` rejects source-specific thresholds.
- `FeatureSignalKind` uses a controlled vocabulary.
- `FeatureSignalValue` uses typed values.
- `FeatureSignalPolicy` rejects source-specific feature signal kinds.
- `FeatureSignalPolicy` rejects lexical-only detectors as acceptance rules.
- `AbstainReasonKind` uses a controlled vocabulary.
- `AbstainReasonFields` uses typed values.
- `AbstainReasonPolicy` validates required fields for each abstain reason kind.
- `AbstainReasonPolicy` uses source-neutral evidence, ambiguity, schema, score, and modality categories.
- `ExtractedUnitProfile` stores measured feature signals.
- `ExtractedUnitProfile` does not store ranker scores.
- `AtomCandidate` stores materialized payload data for one extractor capability.
- `ExtractorDecision` records each active extractor capability outcome.
- Each `ExtractedUnit` has one `ExtractorDecision` per capability in the active extractor capability set.
- Pure abstentions become extractor decisions.
- Pure abstentions do not create atom candidates.
- `AtomCandidate` requires a materialized payload or structured review reason.
- Adapters own files, markdown stores, model calls, PDF extraction, and persistence.
- Extractor selection happens at the extracted-unit level.
- `SourceFamilyAssignment` describes a source profile after extraction.
- `SourceFamilyAssignment` does not gate which atom kinds can be extracted.
- Atom schemas decide whether atom candidates become ledger entries.
- Cue words can be weak features.
- Cue words are never extraction rules by themselves.
- Atom detection uses reusable linguistic, structural, semantic-role, and schema categories.
- Every `ExtractedUnit` has exactly one disposition.
- Headers, chapters, sections, glossary entries, references, and index entries use the `structural` disposition.
- `non-claim` is only for subject-matterless residue.
- `RawSource` remains immutable.
- `EvidenceRecord` remains the source evidence record.
- `SourceRange` remains the source span boundary for page projection.
- `WikiPage` remains generated wiki content.
- `SourceWikiPage` uses `SourceStructureSpine` as its primary page order.
- `SourceStructureSpine` derives from `DocumentStructure`.
- `SourceStructureSection` order follows `SourceOrder`.
- `SynthesisSection` is secondary to `SourceStructureSection`.
- `SynthesisSection` contains coverage-backed `GeneratedPageClaim` units.
- `SourceReviewSection` follows `SourceStructureSection`.
- `SourceReviewSection` follows `SynthesisSection` when a `SynthesisSection` exists.
- `SourceReviewSection` contains `SourceReviewItem` records for `needs-review` entries.
- `SourceReviewSection` contains `DispositionCount` records for `rejected` and `non-claim` units.
- `SourceReviewItem` records contain `SourceCitation` and `ReviewReason`.
- `WikiPageMetadata` carries `ProjectionCoveragePointer`.
- `PageBody` contains `SourceCitation` records.
- `PageBody` displays `SourceCitationLabel` values.
- `PageBody` does not display `InternalSupportId` values.
- `PageBody` does not contain `ProjectionCoveragePointer`.
- `PageBody` does not embed full projection coverage.
- `ProjectionCoverageArtifact` stores `InternalSupportId` values.
- `ProjectionCoverageArtifact` is the machine-checkable authority for page projection support.
- `ProjectionCoverageArtifact` stores `ProjectionSourceSupportSet`.
- `PortableArtifactSet` is the first-class manifest artifact for a portable bundle.
- `PortableArtifactSet` has one `PortableArtifactSetId`.
- `PortableArtifactSet` has one `PortableArtifactSetFingerprint`.
- `PortableArtifactSet` contains `PortableArtifactMember` records for child artifacts.
- `PortableArtifactSet` does not list itself as a `PortableArtifactMember`.
- `PortableArtifactSetFingerprint` changes when child artifact membership changes.
- `PortableArtifactSetFingerprint` excludes `PortableArtifactSetId` and `PortableArtifactSetFingerprint`.
- `PortableArtifactPointer` stores one target artifact id.
- `PortableArtifactPointer` stores one target artifact fingerprint.
- `PortableArtifactPointer` resolves to one `PortableArtifactMember` in `PortableArtifactSet`.
- `PortableArtifactPointer` resolves from that `PortableArtifactMember` to one child artifact.
- `PortableArtifactPointer` target artifact fingerprint matches the resolved artifact fingerprint.
- `TypedArtifactPointerAlias` names one target artifact type.
- Artifact references use `TypedArtifactPointerAlias`.
- Typed artifact fingerprints use `ArtifactFingerprint` rules.
- Typed artifact fingerprint fields are named after the artifact domain type.
- Portable artifacts expose typed artifact fingerprint fields.
- Portable artifacts do not expose persisted fields named `ArtifactFingerprint`.
- `DocumentStructureArtifact` has one `DocumentStructureFingerprint`.
- `ClaimLedgerArtifact` has one `ClaimLedgerFingerprint`.
- `ProjectionCoverageArtifact` has one `ProjectionCoverageFingerprint`.
- `BlockedWriteDiagnosticArtifact` has one `BlockedWriteDiagnosticFingerprint`.
- `ProjectionCoveragePointer` is a `TypedArtifactPointerAlias`.
- `DocumentStructurePointer` is a `TypedArtifactPointerAlias`.
- `ClaimLedgerPointer` is a `TypedArtifactPointerAlias`.
- `LedgerQualityReportPointer` is a `TypedArtifactPointerAlias`.
- `QualityCheckCatalogPointer` is a `TypedArtifactPointerAlias`.
- `LedgerQualityReportArtifact` stores one `LedgerQualityReport`.
- `LedgerQualityReportArtifact` has one `LedgerQualityReportArtifactId`.
- `LedgerQualityReportArtifact` has one `LedgerQualityReportFingerprint`.
- `LedgerQualityReportArtifact` follows `CanonicalOrder`.
- `PortableArtifactSet` contains one `LedgerQualityReportArtifact` for each `LedgerQualityReportFingerprint`.
- `ClaimLedgerArtifact` stores `LedgerQualityReportPointer`.
- `ProjectionCoverageArtifact` stores `LedgerQualityReportPointer`.
- `BlockedWriteDiagnosticArtifact` stores `LedgerQualityReportPointer`.
- `ClaimLedgerArtifact` does not embed `LedgerQualityReport`.
- `ProjectionCoverageArtifact` does not embed `LedgerQualityReport`.
- `BlockedWriteDiagnosticArtifact` does not embed `LedgerQualityReport`.
- Typed artifact fingerprints exclude `LedgerQualityReportPointer`.
- `LedgerQualityReport` stores `QualityFinding` records.
- `LedgerQualityReport` has one `QualityReportScope`.
- Every `QualityFinding` has one `QualityReportScope`.
- Every `QualityFinding` uses its owning `LedgerQualityReport` `QualityReportScope`.
- Every `QualityFinding` has one `QualityFindingSeverity`.
- Every `QualityFinding` has one `QualityFindingReason`.
- `QualityFindingReason` uses `QualityFindingReasonTaxonomy`.
- `QualityFindingReasonTaxonomy` contains source-neutral categories derived from domain object contracts.
- Every `QualityFinding` has one `QualityCheckId`.
- `QualityCheckId` uses `QualityCheckCatalog`.
- `QualityCheckCatalog` stores one `QualityCheckDefinition` for each exact rule that creates `QualityFinding`.
- `QualityCheckCatalogArtifact` stores one `QualityCheckCatalog`.
- `QualityCheckCatalogArtifact` has one `QualityCheckCatalogArtifactId`.
- `QualityCheckCatalogArtifact` has one `QualityCheckCatalogFingerprint`.
- `QualityCheckCatalogArtifact` follows `CanonicalOrder`.
- `PortableArtifactSet` contains one `QualityCheckCatalogArtifact` for each `QualityCheckCatalogFingerprint`.
- `LedgerQualityReport` records with the same `QualityCheckCatalogFingerprint` point to the same `QualityCheckCatalogArtifact`.
- `LedgerQualityReport` stores one `QualityCheckCatalogPointer`.
- `QualityCheckCatalogPointer` stores one `QualityCheckCatalogArtifactId`.
- `QualityCheckCatalogPointer` stores one `QualityCheckCatalogFingerprint`.
- Every `QualityFinding` resolves its `QualityCheckId` through the owning `LedgerQualityReport` `QualityCheckCatalogPointer`.
- Every `QualityCheckDefinition` maps to one `QualityFindingReason`.
- Every `QualityFinding` uses the `QualityFindingReason` from its `QualityCheckDefinition`.
- `ReasonApplicabilityPolicy` maps each `QualityFindingReason` to `AllowedQualityReportScopes`.
- `ReasonApplicabilityPolicy` maps each `QualityFindingReason` to `AllowedQualityFindingSubjectKinds`.
- Every `QualityFinding` uses a `QualityReportScope` allowed by `ReasonApplicabilityPolicy`.
- Every `QualityFinding` uses a `QualityFindingSubjectKind` allowed by `ReasonApplicabilityPolicy`.
- Every `QualityFindingSubject` has one `QualityFindingSubjectKind`.
- Every `QualityFindingSubject` has one `QualityFindingSubjectId`.
- Every `QualityFindingSubject` has one `QualityFindingSubjectField`.
- `QualityFindingSubjectField` uses `whole-object` for object-scoped findings.
- `QualityFindingSubjectKind` uses controlled values derived from domain object contracts.
- Every `QualityFindingLocator` has one `QualityFindingLocatorKind`.
- Every `QualityFindingLocator` stores fields required by `QualityFindingLocatorKind`.
- `QualityFindingLocatorKind` uses controlled portable locator values.
- `QualityFindingSeverityPolicy` maps each `QualityFindingReason` to one `QualityFindingSeverity`.
- `WriteBoundary` uses `QualityFindingSeverityOrder` to derive `PageWriteDecision`.
- `blocking` findings produce `PageWriteDecision` `block-authoritative-write`.
- `warning` findings produce `PageWriteDecision` `write-with-review-work` when no `blocking` finding exists.
- `info` findings produce `PageWriteDecision` `write-authoritative-page` when no `blocking` or `warning` finding exists.
- `block-authoritative-write` produces one `BlockedWriteDiagnosticArtifact`.
- `BlockedWriteDiagnosticArtifact` stores `LedgerQualityReportPointer` that resolves to `QualityReportScope` `blocked-write`.
- `BlockedWriteDiagnosticArtifact` stores no `WikiPage` or `ProjectionCoverageArtifact`.
- `SourceWikiPage` uses one `ProjectionSourceSupport` record.
- `CrossSourceWikiPage` uses two or more `ProjectionSourceSupport` records.
- `ProjectionCoverage` contains `ProjectionCoverageEntry` records.
- Each `ProjectionCoverageEntry` covers one `ProjectionCoverageUnit`.
- `ProjectionCoverageUnitKind` uses a controlled vocabulary.
- A paragraph with multiple `GeneratedPageClaim` units has multiple `ProjectionCoverageEntry` records.
- A `SourceBackedPosition` maps to one `GeneratedPageClaim`.
- A `SourceBackedPosition` resolves to exactly one `ProjectionSourceSupport`.
- Conflicting `SourceBackedPosition` records remain separate `GeneratedPageClaim` units.
- A `CrossSourceRelationship` maps to one `CrossSourceRelationshipId` in one `ProjectionCoverageEntry`.
- A `CrossSourceRelationship` relates two or more `SourceBackedPosition` records.
- A `RenderedTechnicalAtomBlock` maps to one `TechnicalAtomId` in one `ProjectionCoverageEntry`.
- A `SourceReviewItem` maps to one `LedgerEntryId` in one `ProjectionCoverageEntry`.
- A `DispositionCount` maps to one `ExtractedUnitDisposition` in one `ProjectionCoverageEntry`.
- Accepted `TechnicalAtom` records render as `RenderedTechnicalAtomBlock` records.
- `RenderedTechnicalAtomBlock` records appear in the matching `SourceStructureSection`.
- `RenderedTechnicalAtomBlock` order follows `SourceOrder`.
- `RenderedTechnicalAtomBlock` records render `SourceEquivalentPayload`.
- Prose that interprets a `TechnicalAtom` uses separate `GeneratedPageClaim` coverage.
- `GeneratedPageClaim` records carry explanations of `TechnicalAtom` records.
- `index.md` and `log.md` remain current after ingest.
- The generated wiki layer remains disposable test data.
- Production logic follows the `Universal Standard`.

### Authority Model

The authority chain is:

```
RawSource
  -> EvidenceRegistry
  -> DocumentStructureArtifact
  -> ClaimLedgerArtifact
  -> WikiPage
```

`RawSource` remains the final authority.
`EvidenceRegistry` records source evidence.
`DocumentStructureArtifact` records source organization.
`ClaimLedgerArtifact` records subject-matter claims, concepts, relationships, and technical atoms.
`WikiPage` projects `DocumentStructure` and `ClaimLedger` records.

`ExtractedUnitDisposition` has these values.

| Disposition | Meaning |
|---|---|
| `accepted` | Subject-matter content became one or more ledger entries. |
| `structural` | Source organization became one or more structure nodes. |
| `needs-review` | Meaningful content exists, but the system cannot resolve it safely. |
| `rejected` | Candidate extraction failed validation. |
| `non-claim` | Unit contains only subject-matterless residue. |

`non-claim` covers decoration, blank regions, OCR residue, duplicate boilerplate, and repeated footer noise.
`structural` covers chapters, sections, headings, table-of-contents entries, glossary entries, index entries, and reference entries.
Every `SourceWikiPage` reports `DispositionCount` records in `SourceReviewSection`.

### First-Class Domain Objects

| Object | Contract |
|---|---|
| `ExtractedUnitDisposition` | One accounting decision for one extracted unit. |
| `DocumentStructure` | One extracted source organization tree. |
| `StructureNode` | One source organization node with source evidence. |
| `DocumentStructureArtifact` | One persisted source-scoped document structure artifact. |
| `SourceStructureSpine` | One source-ordered page spine derived from `DocumentStructure`. |
| `SourceStructureSection` | One page section derived from one `StructureNode`. |
| `ExtractedUnitProfile` | One measured feature signal set for one extracted unit. |
| `ExtractorCapability` | One reusable atom extraction capability with an evidence contract. |
| `ActiveExtractorCapabilitySet` | One ordered extractor capability set active for one ingest run. |
| `ExtractorDecision` | One extractor outcome for one extracted unit and one extractor capability. |
| `AtomSchemaSet` | One active portable set of atom schemas. |
| `AtomValidator` | One domain validator for atom candidates. |
| `AtomCandidate` | One materialized atom candidate with payload or review reason. |
| `SourceStatement` | One source-bounded statement that can produce multiple ledger entries. |
| `ClaimLedger` | One source-scoped collection of `LedgerEntry` records. |
| `LedgerEntry` | One source-derived record with evidence, normalized text, status, and kind. |
| `DomainConcept` | One concept record with source-neutral facets and evidence. |
| `RelationshipEntry` | One typed relation between ledger records. |
| `TechnicalAtom` | One structured source detail preserved as a ledger entry. |
| `SourceProfile` | One aggregate profile derived from unit profiles and accepted ledger records. |
| `SourceFamilyAssignment` | One scored label set derived from a source profile. |
| `LedgerProjectionPlan` | One page-scoped selection of usable ledger entries. |
| `SourceBackedPosition` | One `GeneratedPageClaim` backed by one `RawSource`. |
| `CrossSourceRelationship` | One projection relation among `SourceBackedPosition` records. |
| `SynthesisSection` | One secondary coverage-backed synthesis section. |
| `SourceReviewSection` | One structured section for `needs-review` entries and disposition counts. |
| `SourceReviewItem` | One structured item for one `LedgerEntry` with `LedgerEntryStatus` `needs-review`. |
| `DispositionCount` | One count for one extracted-unit disposition value. |
| `ProjectionSourceSupport` | One support record for one `RawSource` used by one page projection. |
| `ProjectionSourceSupportSet` | One ordered set of `ProjectionSourceSupport` records for one page projection. |
| `ProjectionCoverage` | One ordered set of `ProjectionCoverageEntry` records for one `WikiPage`. |
| `ProjectionCoverageEntry` | One mapping from one `ProjectionCoverageUnit` to required support fields. |
| `ProjectionCoverageArtifact` | One persisted projection coverage artifact for one wiki page. |
| `BlockedWriteDiagnosticArtifact` | One persisted diagnostic artifact for one blocked authoritative wiki page write. |
| `PortableArtifactSet` | One first-class manifest artifact addressed by deterministic id and fingerprint. |
| `PortableArtifactMember` | One manifest row for one child portable artifact. |
| `PortableArtifactPointer` | One structured reference to one portable artifact id and fingerprint. |
| `TypedArtifactPointerAlias` | One domain-specific pointer name for one target artifact type. |
| `LedgerQualityReport` | One deterministic report for one `QualityReportScope`. |
| `LedgerQualityReportArtifact` | One persisted portable quality report artifact. |
| `LedgerQualityReportPointer` | One artifact reference to a quality report artifact and fingerprint. |
| `QualityReportScope` | One controlled value that scopes one quality report. |
| `QualityFinding` | One deterministic quality report record. |
| `QualityFindingReasonTaxonomy` | One controlled source-neutral set of `QualityFindingReason` values. |
| `QualityCheckCatalog` | One controlled set of exact quality checks. |
| `QualityCheckCatalogArtifact` | One persisted portable catalog of exact quality checks. |
| `QualityCheckCatalogPointer` | One report reference to a quality check catalog artifact and fingerprint. |
| `QualityCheckDefinition` | One exact quality check contract. |
| `QualityFindingSubject` | One structured quality finding subject. |
| `QualityFindingLocator` | One structured quality finding locator. |
| `ReasonApplicabilityPolicy` | One deterministic policy for reason scope and subject applicability. |
| `QualityFindingSeverityPolicy` | One deterministic policy for `QualityFindingSeverity`. |
| `PageWriteDecision` | One write decision derived from `QualityFindingSeverity`. |
| `ReviewWorkItem` | One review item derived from one `QualityFinding` with `QualityFindingSeverity` `warning`. |
| `WriteBoundary` | One domain boundary that maps quality findings to page write decisions. |

Supporting domain objects are `RawSource`, `ExtractedUnit`, `SourceClaim`, `EvidenceRegistry`, `SourceText`, `SourceRange`, `FeatureSignal`, and `EvidenceRecord`.

### Ledger Entry Shape

`LedgerEntry` records use this domain shape.

| Field | Contract |
|---|---|
| `LedgerEntryId` | Stable id inside one `ClaimLedger`. |
| `SourceStatementId` | Source statement that produced the entry. |
| `LedgerEntryKind` | One of `claim`, `event`, `relationship`, `concept`, `quotation`, `technical-atom`, or `source-note`. |
| `LedgerEntryStatus` | One of `usable`, `needs-review`, or `rejected`. |
| `ExtractionConfidence` | One of high, medium, or low. |
| `ConfidenceBasis` | Structured confidence reason. |
| `ReviewReason` | Required when status is needs-review or rejected. |
| `SourceLocator` | Raw source locator. |
| `SourceHash` | Hash of source text used for the entry. |
| `SourceRangeId` | Source range that bounds the entry. |
| `StructureNodeIds` | Structure nodes that contain or contextualize the entry. |
| `EvidenceIds` | Non-empty ordered evidence record ids. |
| `SourceText` | Exact or bounded evidence excerpt. |
| `QuotationText` | Exact source wording when `LedgerEntryKind = quotation`. |
| `NormalizedText` | Source-close text that a page projection can cite. |
| `ResolutionBasis` | Evidence-backed explanation for any resolved subject or fragment. |
| `Subject` | Required for claim-like entries. |
| `Predicate` | Required for claim-like entries. |
| `Object` | Required for claim-like entries. |
| `Polarity` | One of affirmative or negative for claim-like entries. |
| `ClaimForce` | One of asserted, possible, required, forbidden, permitted, or recommended for claim-like entries. |
| `ConditionScope` | One of unconditional, conditional, or exception for claim-like entries. |
| `ConditionText` | Source-derived condition when `ConditionScope = conditional`. |
| `ExceptionText` | Source-derived exception when `ConditionScope = exception`. |
| `TemporalScope` | Structured temporal scope for claim-like entries. |
| `TemporalText` | Exact source wording for temporal scope. |
| `TemporalKind` | One of instant, date, range, duration, sequence, recurring, or unknown. |
| `NormalizedTemporalValue` | Optional normalized temporal value when safe. |
| `TemporalAnchorEntryIds` | Entries that anchor relative times, durations, or sequences. |
| `TemporalConfidence` | One of resolved, partially-resolved, or unresolved. |
| `SpatialScope` | Structured spatial scope for claim-like entries. |
| `SpatialText` | Exact source wording for spatial scope. |
| `SpatialKind` | One of place, region, range, setting, relative-location, or unknown. |
| `NormalizedSpatialValue` | Optional normalized spatial value when safe. |
| `SpatialAnchorEntryIds` | Entries that anchor relative places, ranges, or settings. |
| `SpatialConfidence` | One of resolved, partially-resolved, or unresolved. |
| `ClaimRoleTags` | Existing source-claim role tags. |
| `TechnicalAtomKind` | Structured kind when `LedgerEntryKind = technical-atom`. |
| `ConceptFacets` | Source-neutral facets for concept and event entries. |
| `RelationshipKind` | Typed predicate for relationship entries. |
| `RelatedEntryIds` | Other entries that provide local context. |
| `DerivedEntryIds` | Other entries derived from the same source statement. |
| `StatementRelationship` | Source-local relation to another derived entry. |

### Technical Atom Shape

`TechnicalAtom` records preserve source-equivalent structured data.
The domain stores the payload in a typed shape before any prose page uses it.
The domain defines stable technical atom objects.
`AtomSchemaSet` declares required fields for each technical atom kind.
`AtomValidator` validates atom candidates against the active atom schema set.
Portable atom schema definitions can move between llm-wiki implementations.

| Atom Kind | Required Payload |
|---|---|
| `table` | Raw table text, caption, column order, row order, cell values, notes, parse status, and source locator. |
| `code-block` | Exact code text, language tag, line order, code fence, surrounding explanation locator, parse status, and source locator. |
| `formula` | Exact formula text, notation context locator, and source locator. |
| `procedure` | Ordered steps, preconditions, outputs, and source locator. |
| `rule` | Rule statement, scope, exceptions, and source locator. |
| `worked-example` | Input, operation, output, explanation locator, and source locator. |

The table shape follows the W3C tabular-data principle that row order, column order, and cell metadata are data.
The code-block shape treats whitespace and fence content as part of the source payload.
The formula shape treats symbols and notation as source payload, not prose to paraphrase.

### Table Atom Shape

`table` atoms preserve raw table text and a logical table model.
`RawTableText` is required.
The logical table model is required when parsing succeeds.
The logical table model can be partial when parsing partially succeeds.

| Table Field | Contract |
|---|---|
| `RawTableText` | Exact extracted table text or closest source-equivalent table representation. |
| `TableColumn` | Ordered column with source-derived header text. |
| `TableRow` | Ordered row with source order. |
| `TableCell` | Cell value with row coordinate, column coordinate, and source locator. |
| `TableCaption` | Source-derived caption text. |
| `TableNote` | Source-derived note text. |
| `ParseStatus` | One of parsed, partially-parsed, or unparsed. |
| `SourceLocator` | Source locator for the table. |
| `EvidenceIds` | Evidence records for the table. |
| `ReviewReason` | Required when parse status is partially-parsed or unparsed. |

Table atoms remain usable as exact source references when raw table text is preserved.
Unparsed table atoms require review reason.
Parsed table fields support debugging and query.

### Code Block Atom Shape

`code-block` atoms preserve exact source code text and contextual metadata.
`RawCodeText` is required.
Whitespace is part of raw code text.
Language tag can be source-declared or detected.

| Code Field | Contract |
|---|---|
| `RawCodeText` | Exact source code text including whitespace. |
| `LanguageTag` | Source-declared or detected programming or markup language. |
| `LanguageConfidence` | Required when language tag is detected. |
| `CodeFence` | Source fence marker when present. |
| `LineOrder` | Source line order. |
| `SurroundingExplanationLocator` | Source locator for nearby explanatory text. |
| `ParseStatus` | One of parsed, partially-parsed, or unparsed. |
| `CodeAst` | Optional deterministic parser output. |
| `SourceLocator` | Source locator for the code block. |
| `EvidenceIds` | Evidence records for the code block. |
| `ReviewReason` | Required when exact code text cannot be preserved. |

Code atoms remain usable when raw code text is preserved.
Code AST output is convenience structure.
Code AST output is not source authority.

### Rule Atom Shape

`rule` atoms preserve exact source wording and operational structure.
A rule prescribes, permits, forbids, recommends, calculates, or constrains behavior under a scope.
A claim states what the source presents as true.
The domain detects rules from reusable linguistic, structural, and semantic-role categories.
The domain does not detect rules from bespoke cue-word lists.

| Rule Field | Contract |
|---|---|
| `RuleText` | Exact source wording. |
| `RuleForce` | One of required, forbidden, permitted, recommended, or asserted-constraint. |
| `RuleScope` | Governed entity or context. |
| `RuleTrigger` | Condition that activates the rule. |
| `RuleEffect` | Action, result, calculation, or constraint imposed by the rule. |
| `RuleException` | Source exception. |
| `RuleCandidateProfile` | Source-neutral feature and role profile for a candidate rule. |
| `RuleSchema` | Active atom schema for rule validation. |
| `SourceLocator` | Source locator for the rule. |
| `EvidenceIds` | Evidence records for the rule. |

`RuleCandidateProfile` can include deontic force, imperative mood, conditional scope, threshold expression, exception, procedure shape, lookup table shape, and semantic roles.
Lexical cues can contribute weak features.
Lexical cues cannot accept a rule atom.
`RuleSchema` decides whether a rule candidate becomes a rule atom.
Rule atoms can support linked claim-like entries.
Linked entries must reference the rule atom.
The rule atom remains the authoritative preserved object.
Requirements are rule atoms with required rule force.
Exceptions are rule exception fields when they modify one rule.
Standalone exceptions can become rule atoms or relationship entries when they affect multiple rules.

### Procedure Atom Shape

`procedure` atoms preserve exact source wording and ordered execution structure.
Procedure atoms are separate from rule atoms.
A procedure preserves how to do something.
A rule governs what applies, is allowed, or is required.

| Procedure Field | Contract |
|---|---|
| `ProcedureText` | Exact source wording. |
| `ProcedureGoal` | Source-derived procedure goal. |
| `ProcedureInput` | Source-derived input. |
| `ProcedurePrecondition` | Source-derived precondition. |
| `ProcedureStep` | Ordered step with source locator. |
| `ProcedureOutput` | Source-derived output. |
| `ProcedureException` | Source-derived exception. |
| `SourceLocator` | Source locator for the procedure. |
| `EvidenceIds` | Evidence records for the procedure. |

Procedure steps preserve source order.
Rule atoms can reference procedure steps.
Claim-like entries can reference procedure steps.
The procedure atom remains the authoritative preserved object.

### Worked Example Atom Shape

`worked-example` atoms preserve exact source wording and demonstration structure.
Worked example atoms are separate technical atoms.
Worked example atoms can reference formulas, rules, procedures, tables, and code blocks.

| Worked Example Field | Contract |
|---|---|
| `ExampleText` | Exact source wording. |
| `ExampleSetup` | Source-derived setup. |
| `ExampleInput` | Source-derived input. |
| `ExampleOperation` | Source-derived operation. |
| `ExampleOutput` | Source-derived output. |
| `ExampleExplanation` | Source-derived explanatory text. |
| `ReferencedAtomIds` | Referenced formula, rule, procedure, table, or code atom ids. |
| `SourceLocator` | Source locator for the worked example. |
| `EvidenceIds` | Evidence records for the worked example. |

Worked example atoms preserve pedagogical sequence.
Linked atoms remain authoritative for their own payloads.
The worked example atom remains the authoritative preserved demonstration.

### Formula Atom Shape

`formula` atoms preserve exact source text.
Formula subtype describes what kind of formula the source gives.
Formula surface form describes how the source expresses the formula.

| FormulaSubtype | Meaning |
|---|---|
| `symbolic-formula` | Abstract mathematical, scientific, or engineering relationship. |
| `procedural-formula` | Operational calculation for a rule, manual, game, or workflow result. |

| FormulaSurfaceForm | Meaning |
|---|---|
| `equation` | Source expresses the formula as equation notation. |
| `prose` | Source expresses the formula in natural language. |
| `table-cell` | Source expresses the formula inside a table cell. |
| `list-item` | Source expresses the formula inside a list item. |
| `mixed` | Source combines notation and prose. |

Both formula subtypes can use any formula surface form.
`F = ma` is a `symbolic-formula` with `equation` surface form.
Force is mass times acceleration is a `symbolic-formula` with `prose` surface form.
Damage taken equals attack power minus armor rating is a `procedural-formula` with `prose` surface form.
`Damage Taken = Attack Power - Armor Rating - Modifiers` is a `procedural-formula` with `equation` surface form.

Formula atoms always preserve exact source text, source locator, evidence ids, and notation or rule context.
Parsed formulas are optional convenience structure.
Failed parsing does not remove a formula atom.
Formula atoms can support linked claim, definition, relationship, or measurement entries.
Linked entries require evidence ids.
Linked entries must reference the formula atom.
The formula atom remains the authoritative preserved object.

### Quotation Entry Shape

`quotation` entries preserve exact source wording.
Quotation entries are required when exact wording carries meaning.
Quotation entries can support linked claim, definition, relationship, or concept entries.
Linked entries require evidence ids.
Linked entries must reference the quotation entry.
The quotation entry remains the authoritative preserved wording.
If exact wording matters and cannot be preserved, the entry becomes needs-review.

### Unit Profiles And Atom Candidates

`ExtractedUnitProfile` guides extractor selection for one extracted unit.
It does not decide the source family.
It records source-neutral feature signals.
`FeatureSignalPolicy` validates feature signals before rankers use them.

| FeatureSignal | Meaning |
|---|---|
| `table-density` | The unit contains table-like layout, repeated columns, or cell structure. |
| `code-density` | The unit contains code fences, indentation, API names, or syntax tokens. |
| `formula-density` | The unit contains equations, symbolic notation, or mathematical operators. |
| `entity-date-density` | The unit contains named entities, dates, places, or event phrases. |
| `rule-language-density` | The unit contains modal rules, requirements, exceptions, or constraints. |
| `procedure-density` | The unit contains ordered steps, preconditions, or outputs. |
| `definition-density` | The unit contains term-definition patterns. |
| `relationship-density` | The unit contains cause, sequence, contrast, participation, or location signals. |

`FeatureSignal` stores these fields.

| FeatureSignal Field | Contract |
|---|---|
| `FeatureSignalId` | Stable feature signal id. |
| `FeatureSignalKind` | Controlled reusable category. |
| `FeatureSignalValue` | Typed measured value. |
| `FeatureSignalConfidence` | Measurement confidence. |
| `EvidenceIds` | Evidence records for the signal. |
| `SourceRangeId` | Source range that produced the signal. |

`FeatureSignalKind` must describe reusable linguistic, layout, syntactic, semantic-role, or notation categories.
`FeatureSignalKind` must not name a source, book, author, passage, character, API, game term, or domain-specific phrase.
Lexical cues can contribute to feature signals.
Lexical cues cannot be feature signal kinds by themselves.
Feature signals cannot accept atom candidates by themselves.
Atom schema validation remains the acceptance boundary.
`ExtractedUnitProfile` stores measured feature signals only.
`ExtractedUnitProfile` does not store ranker scores or extraction judgments.
`ExtractorDecision` stores the extractor outcome for one extractor capability.
`AtomCandidate` stores a materialized payload or a structured review reason.
`AtomCandidate` references the feature signals that supported the candidate.

`ExtractorCapability` declares one atom kind and required evidence.
`ActiveExtractorCapabilitySet` contains the extractor capabilities active for one ingest run.
An adapter can rank extractor capabilities for one extracted unit.
The ranker uses feature signals and `RankerScore`.
The ranker applies `CalibrationPolicy` before it writes `CalibrationBucket` values.
The ranker records one extractor decision for each extracted unit and each active extractor capability.
An abstained extractor decision carries abstain reason.
A candidate-produced extractor decision carries atom candidate id.
`AtomValidator` validates atom candidates against the active atom schema set.
Only valid atom candidates can become ledger entries.

`ExtractorDecision` stores these fields.

| ExtractorDecision Field | Contract |
|---|---|
| `ExtractorDecisionId` | Stable extractor decision id. |
| `SourceRangeId` | Source range for the extracted unit. |
| `ExtractorCapabilityId` | Stable extractor capability id. |
| `ExtractorDecisionStatus` | One of `candidate-produced` or `abstained`. |
| `RankerScore` | Required when `ExtractorDecisionStatus` is `abstained`. |
| `CalibrationBucket` | Required when `ExtractorDecisionStatus` is `abstained`. |
| `AbstainReason` | Required when `ExtractorDecisionStatus` is `abstained`. |
| `FeatureSignalIds` | Feature signals that contributed to the decision. |
| `AtomCandidateId` | Required when `ExtractorDecisionStatus` is `candidate-produced`. |

`CalibrationPolicy` stores these fields.

| CalibrationPolicy Field | Contract |
|---|---|
| `ActiveExtractorCapabilitySet` | Extractor capabilities covered by the policy. |
| `RankerScoreRange` | Normalized range from 0.0 through 1.0. |
| `CalibrationBucketSet` | Controlled bucket values. |
| `CalibrationThresholds` | Thresholds keyed by extractor capability id. |

`CalibrationBucketSet` contains `high`, `medium`, and `low`.
`CalibrationThresholds` cannot vary by source title, filename, author, passage, or domain-specific term.

`AbstainReason` stores these fields.

| AbstainReason Field | Contract |
|---|---|
| `AbstainReasonKind` | Controlled reusable reason category. |
| `AbstainReasonFields` | Typed fields required by the reason kind. |
| `EvidenceIds` | Evidence records that support the reason. |

`AbstainReasonPolicy` accepts these reason kinds.

| AbstainReasonKind | Required Typed Field |
|---|---|
| `insufficient-evidence` | `EvidenceRequirement`. |
| `ambiguous-unit` | `AmbiguityBasis`. |
| `schema-mismatch` | `SchemaFailure`. |
| `low-ranker-score` | `ScoreGate`. |
| `unsupported-modality` | `UnsupportedModality`. |

`AtomCandidate` stores these fields.

| AtomCandidate Field | Contract |
|---|---|
| `AtomCandidateId` | Stable atom candidate id. |
| `ExtractorDecisionId` | Extractor decision that produced the candidate. |
| `ExtractorCapabilityId` | Stable extractor capability id. |
| `AtomCandidatePayload` | Typed payload proposed for one technical atom. |
| `RankerScore` | Calibrated source-neutral score. |
| `CalibrationBucket` | Ranker score calibration band. |
| `ReviewReason` | Structured reason when payload cannot be formed from materialized evidence. |
| `FeatureSignalIds` | Feature signals that contributed to the candidate. |
| `EvidenceIds` | Evidence records for the candidate. |

Accepted atom candidates become ledger entries.
Rejected atom candidates become rejected candidates.
Pure abstentions become extractor decisions only.
Atom candidates do not store prompts, transcripts, or raw ranker internals.

| ExtractorCapability | Candidate Atom |
|---|---|
| `table-extractor` | `table` |
| `code-block-extractor` | `code-block` |
| `formula-extractor` | `formula` |
| `procedure-extractor` | `procedure` |
| `rule-extractor` | `rule` |
| `worked-example-extractor` | `worked-example` |

### Source Profiles And Emergent Families

`SourceProfile` aggregates unit profiles, accepted atoms, concepts, and relationships.
`SourceFamilyAssignment` derives optional labels from a source profile.
It supports reporting and coverage checks.
It does not control which extractors run.

| Emergent Label | Evidence Signals |
|---|---|
| `history` | Event records, person records, date records, place records, sequence relationships, cause relationships, coincidence relationships. |
| `coding` | Code atoms, formula atoms, idiom concepts, best-practice concepts, anti-pattern concepts, API concepts. |
| `rules-reference` | Rule atoms, table atoms, procedure atoms, class concepts, setting concepts, exception relationships. |
| `general-prose` | Claim records, concept records, comparison relationships, example relationships, caveat concepts. |
| `unknown` | Source profile confidence stays below the reporting threshold. |

A mixed source can receive multiple labels.
A low-confidence source receives `unknown`.
A label cannot add atom kinds to a ledger.
A label cannot remove atom kinds from a ledger.

### Relationship Kinds

`RelationshipEntry` records use reusable predicates.

| RelationshipKind | Meaning |
|---|---|
| `causes` | One event or condition directly causes another. |
| `coincides-with` | Two records share time or context without a stated causal link. |
| `precedes` | One record comes before another in source order, time, or procedure. |
| `participates-in` | A person, group, class, object, or concept participates in an event or rule. |
| `located-in` | A record has a stated place or setting. |
| `defines` | One record defines a concept, symbol, rule, or term. |
| `exemplifies` | One record gives an example of another record. |
| `constrains` | One record limits another record. |
| `contrasts-with` | One record differs from another by an explicit source comparison. |

The domain can add predicates when a source-neutral facet requires them.
New predicates must describe reusable categories.
New predicates must not encode one source's wording.

`CrossSourceRelationship` records use reusable projection predicates.

| CrossSourceRelationshipKind | Meaning |
|---|---|
| `conflicts-with` | `SourceBackedPosition` records cannot all hold under the same temporal, spatial, and conditional scope. |
| `agrees-with` | `SourceBackedPosition` records assert compatible propositions under compatible scope. |
| `qualifies` | One `SourceBackedPosition` narrows another `SourceBackedPosition` by `ConditionScope`, `TemporalScope`, `SpatialScope`, `ClaimForce`, or `ConceptFacets`. |
| `supersedes` | One `SourceBackedPosition` replaces another by source-stated succession, correction, edition, or revision. |

`CrossSourceRelationshipKind` values are projection predicates.
They do not replace source-derived `RelationshipKind` values.

### Domain Logic

`ExtractedUnitProfile` records source-neutral feature signals for one extracted unit.
`DocumentStructure` associates structure nodes with source ranges.
Adapters rank extractor capabilities for one extracted unit from its feature signals.
Adapters return atom candidates with evidence and scores.
`AtomValidator` validates atom candidates against the active atom schema set.
`ClaimLedgerBuilder` rejects atom candidates that fail atom validation.
`ClaimLedgerBuilder` requires every extracted unit to have one disposition.
`ClaimLedgerBuilder` groups derived entries under a source statement.
`ClaimLedgerBuilder` creates one `LedgerEntry` for each usable source claim.
`ClaimLedgerBuilder` requires claim-like ledger entries to have structured proposition fields.
`ClaimLedgerBuilder` does not treat normalized text alone as a complete claim-like entry.
`Polarity` describes whether the proposition is affirmative or negative.
`ClaimForce` describes the source's force over the proposition.
Prohibitions use affirmative polarity with forbidden claim force when the proposition itself is positive.
Possible claim force means source-stated possibility.
Extraction uncertainty uses extraction confidence and entry status.
The door is not open has negative polarity and asserted claim force.
The character must not move has negative polarity and required claim force.
The character cannot move has affirmative polarity and forbidden claim force.
Do not use mutable globals has affirmative polarity and forbidden claim force.
`TemporalScope` preserves exact temporal wording and structured temporal fields.
Relative temporal scope requires temporal anchor entry ids.
Temporal normalization is optional.
`SpatialScope` preserves exact spatial wording and structured spatial fields.
Relative spatial scope requires spatial anchor entry ids.
Spatial normalization is optional.
`ClaimLedgerBuilder` splits compound source statements into atomic ledger entries.
`ClaimLedgerBuilder` preserves source-local temporal, causal, conditional, and sequential links during splitting.
`ClaimLedgerBuilder` marks a split as needs-review when the split drops required local context.
`ClaimLedgerBuilder` creates one `LedgerEntry` for each valid `TechnicalAtom`.
`ClaimLedgerBuilder` associates ledger entries with containing structure nodes.
`ClaimLedgerBuilder` creates `DomainConcept` records from source-neutral facets.
`ClaimLedgerBuilder` creates `RelationshipEntry` records for supported typed relations.
`ClaimLedgerBuilder` sets `LedgerEntryStatus`.
`ClaimLedgerBuilder` creates `SourceProfile` from unit profiles and accepted ledger records.
`ClaimLedgerBuilder` creates `SourceFamilyAssignment` from source profile signals.
`ConfidencePolicy` uses source-neutral extraction signals.
`ConfidencePolicy` does not score source truth.
`ConfidencePolicy` maps evidence resolution, required fields, validation, parser status, ranker score, competing candidates, and anchor resolution to confidence.
High confidence means evidence resolves, required fields are complete, ambiguity is absent, and validation passed.
Medium confidence means evidence resolves and required fields are complete, but optional interpretation is partial.
Low confidence means source material is preserved or detected, but interpretation is unsafe.
Claim-like entries with low confidence become needs-review.
Exact-preservation atoms can be usable with medium confidence when exact source payload is preserved.

`ResolutionBasis` controls resolved text.
`NormalizedText` can resolve a pronoun when evidence names one possible antecedent.
`NormalizedText` cannot resolve a pronoun when evidence names two possible antecedents.
The domain marks unresolved entries as `needs-review`.

`LedgerProjectionPlanner` selects only `usable` entries.
`LedgerProjectionPlanner` builds `ProjectionSourceSupportSet` for each `WikiPage`.
`LedgerProjectionPlanner` uses one `ProjectionSourceSupport` record for each `SourceWikiPage`.
`LedgerProjectionPlanner` uses two or more `ProjectionSourceSupport` records for each `CrossSourceWikiPage`.
`LedgerProjectionPlanner` creates one `SourceBackedPosition` for each `GeneratedPageClaim` whose `SelectedLedgerEntryIds` resolve to one `ProjectionSourceSupport`.
`LedgerProjectionPlanner` creates `CrossSourceRelationship` records for `SourceBackedPosition` records.
`LedgerProjectionPlanner` builds `SourceStructureSpine` from `DocumentStructure`.
`LedgerProjectionPlanner` orders `SourceStructureSection` records by `SourceOrder`.
`LedgerProjectionPlanner` builds `SourceReviewSection` from `ClaimLedger` and `DocumentStructureArtifact`.
`LedgerProjectionPlanner` routes `needs-review` ledger entries to `SourceReviewItem` records.
`LedgerProjectionPlanner` routes `rejected` and `non-claim` units to `DispositionCount` records.
`LedgerProjectionPlanner` preserves source locators from selected entries.
`WikiPageRenderer` receives a `LedgerProjectionPlan` from the domain.
`WikiPageRenderer` returns `ProjectionCoverage`.
`WikiPageRenderer` renders each `SourceBackedPosition` as a separate `GeneratedPageClaim`.
`WikiPageRenderer` renders each `CrossSourceRelationship` as a separate `ProjectionCoverageUnit`.
`WikiPageRenderer` renders `SourceStructureSection` records before `SynthesisSection` records.
`WikiPageRenderer` renders accepted `TechnicalAtom` records as `RenderedTechnicalAtomBlock` records.
`WikiPageRenderer` places each `RenderedTechnicalAtomBlock` in the matching `SourceStructureSection`.
`WikiPageRenderer` orders `RenderedTechnicalAtomBlock` records by `SourceOrder`.
`WikiPageRenderer` renders `SourceEquivalentPayload` for each `RenderedTechnicalAtomBlock`.
`WikiPageRenderer` renders `SynthesisSection` only when its `GeneratedPageClaim` units have `ProjectionCoverageEntry` records.
`WikiPageRenderer` renders explanations of `TechnicalAtom` records as separate `GeneratedPageClaim` units.
`WikiPageRenderer` renders `SourceReviewSection` after `SourceStructureSection`.
`WikiPageRenderer` renders `SourceReviewSection` after `SynthesisSection` when a `SynthesisSection` exists.
`WikiPageRenderer` renders `SourceReviewItem` records with `SourceCitation` and `ReviewReason`.
`WikiPageRenderer` renders `DispositionCount` records for `rejected` and `non-claim` units.
`WikiPageRenderer` writes `SourceCitation` records into `PageBody`.
`WikiPageRenderer` writes `SourceCitationLabel` values into `SourceCitation` records.
`WikiPageRenderer` writes `ProjectionCoveragePointer` into `WikiPageMetadata`.
`WikiPageRenderer` writes `ProjectionSourceSupportSet` into `ProjectionCoverageArtifact`.
`WikiPageRenderer` does not write `InternalSupportId` values into `PageBody`.
`CoverageOutputPort` receives `ProjectionCoverageArtifact`.
`WriteBoundary` returns `block-authoritative-write` when `LedgerQualityReport` contains a `blocking` finding.
`WriteBoundary` returns `write-with-review-work` when `LedgerQualityReport` contains a `warning` finding and no `blocking` finding.
`WriteBoundary` returns `write-authoritative-page` when `LedgerQualityReport` contains only `info` findings.
`WriteBoundary` returns `write-authoritative-page` when `LedgerQualityReport` contains no `QualityFinding` records.
`WriteBoundary` creates `BlockedWriteDiagnosticArtifact` when `PageWriteDecision` is `block-authoritative-write`.
`DiagnosticOutputPort` receives `BlockedWriteDiagnosticArtifact`.
`DiagnosticStoreAdapter` persists `BlockedWriteDiagnosticArtifact`.
`WikiStoreAdapter` writes no `WikiPage` or `ProjectionCoverageArtifact` when `PageWriteDecision` is `block-authoritative-write`.
`WikiStoreAdapter` writes `WikiPage`, `ProjectionCoverageArtifact`, and `ReviewWorkItem` records when `PageWriteDecision` is `write-with-review-work`.
`WikiStoreAdapter` writes `WikiPage` and `ProjectionCoverageArtifact` when `PageWriteDecision` is `write-authoritative-page`.

`SourceCitation` stores these fields.

| SourceCitation Field | Contract |
|---|---|
| `SourceCitationLabel` | Visible source-facing citation label. |
| `SourceLocator` | Source locator represented by the citation. |
| `PageTextRange` | Page body span for the citation. |

`ProjectionCoverageArtifact` stores these fields.

| ProjectionCoverageArtifact Field | Contract |
|---|---|
| `ProjectionCoverageArtifactId` | Stable id for one `ProjectionCoverageArtifact`. |
| `ProjectionCoverageFingerprint` | `ArtifactFingerprint` for canonical projection coverage artifact contents. |
| `WikiPageLocator` | Wiki page covered by this artifact. |
| `PageBodyHash` | Hash of the `PageBody` covered by this artifact. |
| `LedgerQualityReportPointer` | Reference to the page-projection quality report artifact. |
| `ProjectionSourceSupportSet` | Ordered `ProjectionSourceSupport` records used by projection. |
| `ProjectionCoverage` | Ordered `ProjectionCoverageEntry` records. |

`BlockedWriteDiagnosticArtifact` stores these fields.

| BlockedWriteDiagnosticArtifact Field | Contract |
|---|---|
| `BlockedWriteDiagnosticArtifactId` | Stable id for one `BlockedWriteDiagnosticArtifact`. |
| `PageWriteDecision` | The value `block-authoritative-write`. |
| `LedgerQualityReportPointer` | Reference to the blocked-write quality report artifact. |
| `ClaimLedgerPointer` | Reference to the claim ledger artifact used by the blocked write. |
| `WikiPageLocator` | Intended wiki page locator. |
| `BlockedWriteDiagnosticFingerprint` | `ArtifactFingerprint` for blocked write diagnostic contents. |

`ProjectionSourceSupport` stores these fields.

| ProjectionSourceSupport Field | Contract |
|---|---|
| `ProjectionSourceSupportId` | Stable id for one `ProjectionSourceSupport`. |
| `SourceHash` | Source hash for the supported source. |
| `SourceLocator` | Source locator for the supported source. |
| `ClaimLedgerPointer` | Reference to the claim ledger artifact used by projection. |
| `DocumentStructurePointer` | Reference to the document structure artifact used by projection. |

`ProjectionSourceSupportSet` order follows the first `SourceCitation` `PageTextRange` for each source.
`ProjectionSourceSupportSet` order uses `ClaimLedgerPointer` as a tie-breaker.

`ProjectionCoverageEntry` stores these fields.

| ProjectionCoverageEntry Field | Contract |
|---|---|
| `ProjectionCoverageEntryId` | Stable projection coverage entry id. |
| `ProjectionCoverageUnitKind` | One of `generated-page-claim`, `rendered-technical-atom-block`, `source-review-item`, `disposition-count`, or `cross-source-relationship`. |
| `PageTextRange` | Page body span covered by the entry. |
| `SelectedLedgerEntryIds` | Required when unit kind is `generated-page-claim`. |
| `TechnicalAtomId` | Required when unit kind is `rendered-technical-atom-block`. |
| `LedgerEntryId` | Required when unit kind is `source-review-item`. |
| `ExtractedUnitDisposition` | Required when unit kind is `disposition-count`. |
| `CrossSourceRelationshipId` | Required when unit kind is `cross-source-relationship`. |

`GeneratedPageClaim` units use `generated-page-claim`.
`RenderedTechnicalAtomBlock` units use `rendered-technical-atom-block`.
`SourceReviewItem` units use `source-review-item`.
`DispositionCount` units use `disposition-count`.
`CrossSourceRelationship` units use `cross-source-relationship`.
One paragraph can contain multiple `GeneratedPageClaim` units.
Each `GeneratedPageClaim` gets one `ProjectionCoverageEntry`.
One `RenderedTechnicalAtomBlock` gets one `ProjectionCoverageEntry`.
One `SourceReviewItem` gets one `ProjectionCoverageEntry`.
One `DispositionCount` gets one `ProjectionCoverageEntry`.
One `CrossSourceRelationship` gets one `ProjectionCoverageEntry`.
Prose that interprets a `TechnicalAtom` gets a separate `GeneratedPageClaim` entry.

`CrossSourceRelationship` stores these fields.

| CrossSourceRelationship Field | Contract |
|---|---|
| `CrossSourceRelationshipId` | Stable id for one `CrossSourceRelationship`. |
| `CrossSourceRelationshipKind` | Projection relation kind. |
| `RelatedProjectionCoverageEntryIds` | Related `SourceBackedPosition` entries. |
| `RelatedEntryIds` | Ledger entries that support the relation. |
| `ProjectionCoverageEntryId` | `ProjectionCoverageEntry` for the relation. |

`SourceReviewItem` stores these fields.

| SourceReviewItem Field | Contract |
|---|---|
| `LedgerEntryId` | `LedgerEntry` with `LedgerEntryStatus` `needs-review`. |
| `SourceCitation` | Visible citation for the item. |
| `ReviewReason` | Structured reason for review. |
| `ProjectionCoverageEntryId` | `ProjectionCoverageEntry` for the item. |

`DispositionCount` stores these fields.

| DispositionCount Field | Contract |
|---|---|
| `ExtractedUnitDisposition` | Extracted unit disposition counted by the record. |
| `DispositionCountValue` | Number of extracted units with the disposition. |
| `ProjectionCoverageEntryId` | `ProjectionCoverageEntry` for the count. |

`RenderedTechnicalAtomBlock` stores these fields.

| RenderedTechnicalAtomBlock Field | Contract |
|---|---|
| `TechnicalAtomId` | `TechnicalAtom` rendered by the block. |
| `SourceStructureSection` | `SourceStructureSection` that contains the block. |
| `SourceOrder` | `SourceOrder` for the block inside the section. |
| `SourceEquivalentPayload` | `SourceEquivalentPayload` rendered by the block. |
| `ProjectionCoverageEntryId` | `ProjectionCoverageEntry` for the block. |

### Ports

Ports keep the `ClaimLedger` portable.
Each port moves explicit records across the boundary.

| Port | Direction | Contract |
|---|---|---|
| `SourceArtifactInputPort` | Into domain | Supplies `DocumentStructure`, `SourceClaim`, `EvidenceRegistry`, `ExtractedUnitProfile`, `ExtractorDecision`, and `AtomCandidate` records. |
| `SchemaInputPort` | Into domain | Supplies `AtomSchemaSet`, `ActiveExtractorCapabilitySet`, `FeatureSignalPolicy`, `AbstainReasonPolicy`, `CalibrationPolicy`, `ConfidencePolicy`, and page contracts. |
| `LedgerOutputPort` | Out of domain | Receives `ClaimLedger` records. |
| `ProjectionInputPort` | Into domain | Supplies `DocumentStructure` records, `ClaimLedger` records, and a target `WikiPage` contract. |
| `ProjectionOutputPort` | Out of domain | Receives `LedgerProjectionPlan` and projection constraints. |
| `CoverageOutputPort` | Out of adapter | Receives `ProjectionCoverageArtifact` from page rendering. |
| `DiagnosticOutputPort` | Out of domain | Receives `BlockedWriteDiagnosticArtifact` from `WriteBoundary`. |
| `QualityReportOutputPort` | Out of domain | Receives `LedgerQualityReport` records. |
| `ArtifactManifestOutputPort` | Out of domain | Receives `PortableArtifactSet` records from `ArtifactManifestBuilder`. |

The domain module defines these port contracts.
Adapters implement the contracts for a specific llm-wiki repository.

### Adapters

`SourceExtractionAdapter` reads raw files and creates source artifacts.
`ModelAdapter` calls an LLM and returns structured artifacts, scores, and atom candidates.
`SchemaAdapter` reads atom schema set, active extractor capability set, feature signal policy, abstain reason policy, `CalibrationPolicy`, confidence policy, and page body contracts.
`LedgerStoreAdapter` persists `ClaimLedgerArtifact`.
`QualityReportStoreAdapter` persists `LedgerQualityReportArtifact`.
`DocumentStructureStoreAdapter` persists `DocumentStructureArtifact`.
`DiagnosticStoreAdapter` persists `BlockedWriteDiagnosticArtifact`.
`ArtifactManifestStoreAdapter` persists `PortableArtifactSet`.
`WikiStoreAdapter` writes generated `WikiPage` markdown.
`WikiStoreAdapter` writes `ProjectionCoverageArtifact`.
`LogAdapter` updates `index.md` and `log.md`.

Adapters can vary between llm-wiki implementations.
The `DomainModule` cannot vary to match one adapter's storage format.

### Flow

Ledger build:

```
SourceExtractionAdapter -> SourceArtifactInputPort
ModelAdapter            -> SourceArtifactInputPort
SchemaAdapter           -> SchemaInputPort
SourceArtifactInputPort -> DomainModule
SchemaInputPort         -> DomainModule
DomainModule            -> LedgerOutputPort
DomainModule            -> QualityReportOutputPort
DocumentStructureStoreAdapter -> DocumentStructureArtifact
LedgerStoreAdapter      -> ClaimLedgerArtifact
QualityReportOutputPort -> QualityReportStoreAdapter
QualityReportStoreAdapter -> LedgerQualityReportArtifact
```

Source page projection:

```
DocumentStructureStoreAdapter -> ProjectionInputPort
LedgerStoreAdapter            -> ProjectionInputPort
SchemaAdapter                 -> ProjectionInputPort
ProjectionInputPort           -> DomainModule
DomainModule                  -> ProjectionOutputPort
DomainModule                  -> QualityReportOutputPort
WikiStoreAdapter              -> WikiPage
WikiStoreAdapter              -> ProjectionCoverageArtifact
WikiStoreAdapter              -> CoverageOutputPort
QualityReportOutputPort       -> QualityReportStoreAdapter
QualityReportStoreAdapter     -> LedgerQualityReportArtifact
```

Quality reporting:

```
ClaimLedger        -> DomainModule
ProjectionCoverageArtifact -> DomainModule
WikiPage           -> DomainModule
DomainModule             -> QualityReportOutputPort
QualityReportOutputPort  -> QualityReportStoreAdapter
QualityReportStoreAdapter -> LedgerQualityReportArtifact
```

Blocked page write:

```
LedgerQualityReport -> WriteBoundary
WriteBoundary       -> DiagnosticOutputPort
DiagnosticOutputPort -> DiagnosticStoreAdapter
```

Portable bundle export:

```
Portable artifact descriptors -> ArtifactManifestBuilder
ArtifactManifestBuilder       -> ArtifactManifestOutputPort
ArtifactManifestOutputPort    -> ArtifactManifestStoreAdapter
ArtifactManifestStoreAdapter  -> PortableArtifactSet
```

### Ledger Artifact Portability

`PortableArtifactSet` is the import and export root for a portable bundle.
It is a manifest artifact, not a generated wiki page.
It lists child portable artifacts by artifact kind, id, fingerprint, and format.
It does not embed child artifact bodies.
It can be verified before any child artifact is imported.

`DocumentStructureArtifact` is a sibling artifact to `ClaimLedgerArtifact`.
It stores structure nodes and extracted-unit dispositions.
It can be imported without importing page prose.

`QualityCheckCatalogArtifact` is a sibling artifact to `ClaimLedgerArtifact`.
It stores the exact quality checks used by one or more `LedgerQualityReport` records.
The `PortableArtifactSet` addresses `QualityCheckCatalogArtifact` records by `QualityCheckCatalogFingerprint`.
The `PortableArtifactSet` contains one `QualityCheckCatalogArtifact` for each `QualityCheckCatalogFingerprint`.
`LedgerQualityReport` records with the same `QualityCheckCatalogFingerprint` reference the same `QualityCheckCatalogArtifact`.
It can be imported without importing source text, ledger entries, or page prose.

`LedgerQualityReportArtifact` is a sibling artifact to `ClaimLedgerArtifact`.
It stores the full `LedgerQualityReport` body.
The `PortableArtifactSet` addresses `LedgerQualityReportArtifact` records by `LedgerQualityReportFingerprint`.
The `PortableArtifactSet` contains one `LedgerQualityReportArtifact` for each `LedgerQualityReportFingerprint`.
`ClaimLedgerArtifact` references `LedgerQualityReportArtifact` records with `LedgerQualityReportPointer`.
`ProjectionCoverageArtifact` references `LedgerQualityReportArtifact` records with `LedgerQualityReportPointer`.
`BlockedWriteDiagnosticArtifact` references `LedgerQualityReportArtifact` records with `LedgerQualityReportPointer`.
`ClaimLedgerArtifact` does not embed `LedgerQualityReport`.
`ProjectionCoverageArtifact` does not embed `LedgerQualityReport`.
`BlockedWriteDiagnosticArtifact` does not embed `LedgerQualityReport`.

`ClaimLedgerArtifact` stores portable records.
It is one canonical JSON document per source.
It includes all ledger entries and extracted-unit dispositions.
It includes needs-review entries with evidence and review reason.
It includes extractor decisions as `ExtractorDecisions`.
It includes rejected candidates as `RejectedCandidates`.
It does not store local absolute paths as authority.
It does not store Python class paths as authority.
It does not store prompts as authority.
It does not store generated page prose as authority.

Portable ids use these deterministic inputs.

| Id | Deterministic Inputs |
|---|---|
| `ClaimLedgerId` | `SourceHash`. |
| `LedgerEntryId` | `SourceHash`, `SourceRangeId`, `LedgerEntryKind`, and `EntryFingerprint`. |
| `ExtractorDecisionId` | `SourceHash`, `SourceRangeId`, `ExtractorCapabilityId`, and `ExtractorDecisionStatus`. |
| `AtomCandidateId` | `SourceHash`, `SourceRangeId`, `ExtractorCapabilityId`, and `PayloadFingerprint` or `ReviewReason`. |
| `TechnicalAtomId` | `SourceHash`, `SourceRangeId`, `TechnicalAtomKind`, and `PayloadFingerprint`. |
| `RelationshipEntryId` | Source entry id, `RelationshipKind`, target entry id, and `EvidenceIds`. |
| `StructureNodeId` | `SourceHash`, `SourceRangeId`, structure node kind, and `HeadingTextFingerprint`. |
| `CrossSourceRelationshipId` | `WikiPageLocator`, `CrossSourceRelationshipKind`, `RelatedProjectionCoverageEntryIds`, and `RelatedEntryIds`. |
| `ProjectionSourceSupportId` | `SourceHash`, `ClaimLedgerPointer`, and `DocumentStructurePointer`. |
| `ProjectionCoverageArtifactId` | `WikiPageLocator`, `PageBodyHash`, and `ProjectionSourceSupportSet`. |
| `ProjectionCoverageEntryId` | `ProjectionCoverageArtifactId`, `ProjectionCoverageUnitKind`, `PageTextRange`, `SelectedLedgerEntryIds`, `TechnicalAtomId`, `LedgerEntryId`, `ExtractedUnitDisposition`, and `CrossSourceRelationshipId` when present. |
| `BlockedWriteDiagnosticArtifactId` | `WikiPageLocator`, `ClaimLedgerPointer`, and `PageWriteDecision`. |
| `QualityCheckCatalogArtifactId` | `QualityCheckCatalogFingerprint`. |
| `LedgerQualityReportArtifactId` | `LedgerQualityReportFingerprint`. |
| `PortableArtifactSetId` | `PortableArtifactSetFingerprint`. |

Portable artifacts use this canonical order.

| Collection | CanonicalOrder |
|---|---|
| `Entries` | Source order, then `LedgerEntryKind`, then `LedgerEntryId`. |
| `ExtractorDecisions` | Source order, then `ExtractorCapabilityId`, then `ExtractorDecisionId`. |
| `RejectedCandidates` | Source order, then candidate kind, then candidate fingerprint. |
| `ExtractedUnitDisposition` records | Source order. |
| `StructureNodeIds` | Nearest containing structure node first, then ancestors outward. |
| `EvidenceIds` | Source order. |
| `RelatedProjectionCoverageEntryIds` | `PageTextRange`, then `ProjectionCoverageEntryId`. |
| `ProjectionSourceSupportSet` | First `SourceCitation` `PageTextRange`, then `ClaimLedgerPointer`. |
| `PortableArtifactMember` | `PortableArtifactKind`, then target artifact id, then target artifact fingerprint. |
| `QualityCheckCatalog` | `QualityCheckId`. |
| `QualityFinding` | `QualityFindingSeverityOrder`, then `QualityFindingReason`, then `QualityFindingSubjectKind`, then `QualityFindingSubjectId`, then `QualityCheckId`. |
| JSON object keys | Sorted key order. |

Canonical artifact bodies exclude run timestamps.
Source-derived dates remain valid source data.
Typed artifact fingerprints exclude the artifact's own typed artifact fingerprint field.
Typed artifact fingerprints exclude artifact id fields whose deterministic input is that fingerprint.

`PortableArtifactSet` stores these portable fields.

| Field | Contract |
|---|---|
| `PortableArtifactSetId` | Stable id for one portable artifact set manifest. |
| `PortableArtifactSetFingerprint` | `ArtifactFingerprint` for canonical portable artifact set manifest contents. |
| `ArtifactFormat` | Canonical JSON document. |
| `CanonicalOrder` | Deterministic ordering for member records and object keys. |
| `PortableArtifactMember` records | Ordered child artifact manifest rows. |

`PortableArtifactMember` stores these fields.

| Field | Contract |
|---|---|
| `PortableArtifactKind` | Controlled artifact domain type. |
| Target artifact id | Stable id for the child artifact. |
| Target artifact fingerprint | Typed artifact fingerprint for the child artifact. |
| `ArtifactFormat` | Canonical artifact format expected for the child artifact. |

`PortableArtifactKind` contains these values.

| PortableArtifactKind | Contract |
|---|---|
| `portable-artifact-set` | The root manifest artifact. This kind is not valid for `PortableArtifactMember` records. |
| `document-structure-artifact` | One document structure artifact. |
| `claim-ledger-artifact` | One claim ledger artifact. |
| `projection-coverage-artifact` | One projection coverage artifact. |
| `ledger-quality-report-artifact` | One ledger quality report artifact. |
| `quality-check-catalog-artifact` | One quality check catalog artifact. |
| `blocked-write-diagnostic-artifact` | One blocked write diagnostic artifact. |

`DocumentStructureArtifact` stores these portable fields.

| Field | Contract |
|---|---|
| `DocumentStructureArtifactId` | Stable id for one document structure artifact. |
| `DocumentStructureFingerprint` | `ArtifactFingerprint` for document structure artifact contents. |
| `ArtifactFormat` | Canonical JSON document. |
| `CanonicalOrder` | Deterministic ordering for structure records and object keys. |
| `StructureNodeIds` | Ordered ids for structure nodes. |
| `ExtractedUnitDisposition` records | Ordered source unit dispositions. |

`QualityCheckCatalogArtifact` stores these portable fields.

| Field | Contract |
|---|---|
| `QualityCheckCatalogArtifactId` | Stable id for one quality check catalog artifact. |
| `QualityCheckCatalogFingerprint` | `ArtifactFingerprint` for canonical quality check catalog and policy contents. |
| `ArtifactFormat` | Canonical JSON document. |
| `CanonicalOrder` | Deterministic ordering for catalog records and object keys. |
| `QualityCheckCatalog` | Ordered `QualityCheckDefinition` records. |
| `ReasonApplicabilityPolicy` | Source-neutral reason scope and subject applicability policy used by the catalog. |
| `QualityFindingSeverityPolicy` | Source-neutral severity policy used by the catalog. |

`LedgerQualityReportArtifact` stores these portable fields.

| Field | Contract |
|---|---|
| `LedgerQualityReportArtifactId` | Stable id for one quality report artifact. |
| `LedgerQualityReportFingerprint` | `ArtifactFingerprint` for canonical quality report contents. |
| `ArtifactFormat` | Canonical JSON document. |
| `CanonicalOrder` | Deterministic ordering for report records and object keys. |
| `LedgerQualityReport` | Full quality report body. |

`ClaimLedgerArtifact` stores these portable fields.

| Field | Contract |
|---|---|
| `ClaimLedgerId` | Stable id for one source ledger. |
| `ArtifactFormat` | Canonical JSON document. |
| `CanonicalOrder` | Deterministic ordering for arrays and object keys. |
| `DocumentStructurePointer` | Reference to the sibling document structure artifact. |
| `SourceLocator` | Portable source locator. |
| `SourceHash` | Hash of source bytes or extracted source text. |
| `EvidenceRegistryHash` | Hash of the evidence registry artifact. |
| `ClaimLedgerFingerprint` | `ArtifactFingerprint` for domain-relevant claim ledger contents. |
| `SourceProfile` | Aggregate profile derived from accepted records and unit profiles. |
| `SourceFamilyAssignment` | Optional scored labels derived from the source profile. |
| `LedgerQualityReportPointer` | Reference to the ledger-build quality report artifact. |
| `Entries` | Ordered `LedgerEntry` records. |
| `ExtractorDecisions` | Ordered extractor decision records retained for audit. |
| `RejectedCandidates` | Rejected atom or claim candidates retained for completeness and future review. |

Any llm-wiki implementation can import `ClaimLedgerArtifact` when it can resolve `SourceLocator` and `EvidenceIds`.
An implementation rejects import when `SourceLocator` does not resolve.
An implementation rejects import when `EvidenceIds` do not resolve.
An implementation rejects import when the raw source hash mismatches.
An implementation rejects import when the evidence registry hash mismatches.
An implementation rejects import when a present `DocumentStructurePointer` fingerprint mismatches.
A claim ledger imports as fully contextualized when the matching `DocumentStructureArtifact` resolves.
A claim ledger imports as decontextualized only during external import when the `DocumentStructureArtifact` is absent.
Normal ingest fails when `DocumentStructureArtifact` is absent.
Future review workflows can use needs-review entries and rejected candidates.
Future review workflows are outside this DDD.
Review-derived wiki pages can exist.
Review-derived source-page claims still need ledger evidence.
`needs-review` entries appear as `SourceReviewItem` records.
`rejected` units appear as `DispositionCount` records.
`non-claim` units appear as `DispositionCount` records.

### Quality Rules

`LedgerQualityReport` counts entries by status, kind, source profile, family assignment, and projection coverage within its `QualityReportScope`.

`LedgerQualityReport` stores these fields.

| LedgerQualityReport Field | Contract |
|---|---|
| `QualityReportScope` | One of `ledger-build`, `page-projection`, `blocked-write`, or `cross-source-projection`. |
| `QualityCheckCatalogPointer` | Reference to the exact catalog artifact used to create the report. |
| `QualityFinding` | Ordered records whose `QualityReportScope` equals the report `QualityReportScope`. |

`PortableArtifactPointer` stores these fields.

| PortableArtifactPointer Field | Contract |
|---|---|
| Target artifact id | Stable id for the referenced artifact. |
| Target artifact fingerprint | Exact fingerprint expected for the referenced artifact. |

`TypedArtifactPointerAlias` contains these values.

| TypedArtifactPointerAlias | Target Artifact Id | Target Artifact Fingerprint |
|---|---|---|
| `ProjectionCoveragePointer` | `ProjectionCoverageArtifactId` | `ProjectionCoverageFingerprint` |
| `DocumentStructurePointer` | `DocumentStructureArtifactId` | `DocumentStructureFingerprint` |
| `ClaimLedgerPointer` | `ClaimLedgerId` | `ClaimLedgerFingerprint` |
| `LedgerQualityReportPointer` | `LedgerQualityReportArtifactId` | `LedgerQualityReportFingerprint` |
| `QualityCheckCatalogPointer` | `QualityCheckCatalogArtifactId` | `QualityCheckCatalogFingerprint` |

`LedgerQualityReportPointer` stores these fields.

| LedgerQualityReportPointer Field | Contract |
|---|---|
| `LedgerQualityReportArtifactId` | Target artifact id. |
| `LedgerQualityReportFingerprint` | Target artifact fingerprint. |

`QualityReportScope` values have these contracts.

| QualityReportScope | Contract |
|---|---|
| `ledger-build` | Checks source-scoped ledger artifacts before page projection. |
| `page-projection` | Checks one `SourceWikiPage` and its `ProjectionCoverageArtifact`. |
| `blocked-write` | Checks one `BlockedWriteDiagnosticArtifact` for a withheld authoritative write. |
| `cross-source-projection` | Checks one `CrossSourceWikiPage` and its cross-source relationships. |

`QualityFinding` stores these fields.

| QualityFinding Field | Contract |
|---|---|
| `QualityCheckId` | Stable id for the exact violated quality check. |
| `QualityReportScope` | Same value as the owning `LedgerQualityReport`. |
| `QualityFindingSeverity` | One of `blocking`, `warning`, or `info`. |
| `QualityFindingReason` | Controlled reason kind. |
| `QualityFindingSubject` | Structured subject for the finding. |
| `QualityFindingLocator` | Structured locator for the finding. |
| `ReviewReason` | Required when `QualityFindingSeverity` is `warning`. |

`QualityCheckDefinition` stores these fields.

| QualityCheckDefinition Field | Contract |
|---|---|
| `QualityCheckId` | Stable id for one exact quality check. |
| `QualityFindingReason` | Reason category produced by the check. |
| `AllowedQualityReportScopes` | `QualityReportScope` values allowed for the check. |
| `AllowedQualityFindingSubjectKinds` | `QualityFindingSubjectKind` values allowed for the check. |
| `QualityFindingSubjectField` | Domain field name or `whole-object` checked by the rule. |

`QualityCheckId` uses source-neutral domain vocabulary.
`QualityCheckId` uses domain object names, domain field names, and invariant names.
`QualityCheckId` stays stable across renamed-domain variants.
`QualityCheckCatalog` contains one `QualityCheckDefinition` for each exact rule that creates `QualityFinding`.

`QualityCheckCatalogPointer` stores these fields.

| QualityCheckCatalogPointer Field | Contract |
|---|---|
| `QualityCheckCatalogArtifactId` | Target artifact id. |
| `QualityCheckCatalogFingerprint` | Target artifact fingerprint. |

`QualityFindingSubject` stores these fields.

| QualityFindingSubject Field | Contract |
|---|---|
| `QualityFindingSubjectKind` | Controlled domain object kind. |
| `QualityFindingSubjectId` | Stable id for the subject object. |
| `QualityFindingSubjectField` | Domain field name or `whole-object`. |

`QualityFindingSubjectKind` contains these values.

| Domain Area | QualityFindingSubjectKind |
|---|---|
| Artifact | `portable-artifact-set`, `portable-artifact-member`, `portable-artifact-pointer`, `typed-artifact-pointer-alias`. |
| Source | `raw-source`, `source-range`, `document-structure-artifact`, `structure-node`, `extracted-unit`, `source-citation`. |
| Extractor | `extractor-capability`, `active-extractor-capability-set`, `extractor-decision`, `atom-candidate`, `feature-signal`, `abstain-reason`, `ranker-score`, `calibration-bucket`, `calibration-threshold`, `calibration-policy`, `confidence-policy`. |
| Ledger | `claim-ledger-artifact`, `ledger-entry`, `source-statement`, `technical-atom`, `domain-concept`, `relationship-entry`. |
| Projection | `wiki-page`, `page-body`, `projection-source-support`, `projection-coverage-artifact`, `projection-coverage-entry`, `generated-page-claim`, `rendered-technical-atom-block`, `source-structure-section`, `synthesis-section`, `source-review-section`, `source-review-item`, `disposition-count`, `source-backed-position`, `cross-source-relationship`. |
| Quality | `quality-report`, `ledger-quality-report-artifact`, `quality-finding`, `quality-check-catalog-artifact`, `blocked-write-diagnostic-artifact`. |
| Classification | `source-profile`, `source-family-assignment`. |

`QualityFindingLocator` stores these fields.

| QualityFindingLocator Field | Contract |
|---|---|
| `QualityFindingLocatorKind` | Controlled portable locator kind. |
| `SourceLocator` | Required for `source-locator`. |
| `SourceHash` | Required for `source-range-locator`. |
| `SourceRangeId` | Required for `source-range-locator`. |
| `WikiPageLocator` | Required for `wiki-page-locator` and `page-text-range-locator`. |
| `PageTextRange` | Required for `page-text-range-locator`. |
| `ArtifactLocatorFingerprint` | Required for `artifact-locator`. |
| `QualityFindingSubjectId` | Required for `artifact-locator` and `domain-id-locator`. |

`QualityFindingLocatorKind` contains these values.

| QualityFindingLocatorKind | Contract |
|---|---|
| `source-locator` | Resolves through `SourceLocator`. |
| `source-range-locator` | Resolves through `SourceHash` and `SourceRangeId`. |
| `wiki-page-locator` | Resolves through `WikiPageLocator`. |
| `page-text-range-locator` | Resolves through `WikiPageLocator` and `PageTextRange`. |
| `artifact-locator` | Resolves through `QualityFindingSubjectKind`, `QualityFindingSubjectId`, and `ArtifactLocatorFingerprint`. |
| `domain-id-locator` | Resolves through `QualityFindingSubjectKind` and `QualityFindingSubjectId`. |

`QualityFindingSeverity` values have these effects.

| QualityFindingSeverity | PageWriteDecision |
|---|---|
| `blocking` | `block-authoritative-write`. |
| `warning` | `write-with-review-work`. |
| `info` | `write-authoritative-page`. |

`QualityFindingReasonTaxonomy` contains these values.

| QualityFindingReason | QualityFindingSeverity | Contract |
|---|---|---|
| `traceability-failure` | `blocking` | A page unit, ledger entry, or citation cannot resolve to required source support. |
| `coverage-gap` | `blocking` | A required domain object does not appear in ledger, projection coverage, or review coverage. |
| `technical-atom-fidelity-failure` | `blocking` | A `TechnicalAtom` lacks required raw payload, logical payload, exact payload, or source-equivalent payload. |
| `schema-invalid` | `blocking` | A persisted artifact violates required domain fields or field types. |
| `controlled-vocabulary-invalid` | `blocking` | A controlled vocabulary value is outside its declared vocabulary. |
| `canonical-order-invalid` | `blocking` | A persisted artifact violates `CanonicalOrder` or fingerprint rules. |
| `page-hash-invalid` | `blocking` | `WikiPageMetadata` and `ProjectionCoverageArtifact` do not agree on projected page identity. |
| `review-required` | `warning` | Supported material requires user review and a `ReviewReason`. |
| `audit-metric` | `info` | A report entry records counts or distribution metrics. |

`ReasonApplicabilityPolicy` contains these values.

| QualityFindingReason | AllowedQualityReportScopes | AllowedQualityFindingSubjectKinds |
|---|---|---|
| `traceability-failure` | `ledger-build`, `page-projection`, `cross-source-projection` | `raw-source`, `source-range`, `source-citation`, `claim-ledger-artifact`, `ledger-entry`, `source-statement`, `technical-atom`, `domain-concept`, `relationship-entry`, `wiki-page`, `page-body`, `projection-source-support`, `projection-coverage-artifact`, `projection-coverage-entry`, `generated-page-claim`, `rendered-technical-atom-block`, `source-review-item`, `source-backed-position`, `cross-source-relationship`. |
| `coverage-gap` | `ledger-build`, `page-projection`, `cross-source-projection` | `document-structure-artifact`, `structure-node`, `extracted-unit`, `extractor-decision`, `claim-ledger-artifact`, `ledger-entry`, `technical-atom`, `wiki-page`, `page-body`, `projection-coverage-artifact`, `projection-coverage-entry`, `generated-page-claim`, `rendered-technical-atom-block`, `source-structure-section`, `synthesis-section`, `source-review-section`, `source-review-item`, `disposition-count`, `source-backed-position`, `cross-source-relationship`. |
| `technical-atom-fidelity-failure` | `ledger-build`, `page-projection`, `cross-source-projection` | `atom-candidate`, `technical-atom`, `rendered-technical-atom-block`, `projection-coverage-entry`, `generated-page-claim`. |
| `schema-invalid` | `ledger-build`, `page-projection`, `blocked-write`, `cross-source-projection` | Every `QualityFindingSubjectKind` value. |
| `controlled-vocabulary-invalid` | `ledger-build`, `page-projection`, `blocked-write`, `cross-source-projection` | Every `QualityFindingSubjectKind` value. |
| `canonical-order-invalid` | `ledger-build`, `page-projection`, `blocked-write`, `cross-source-projection` | `portable-artifact-set`, `portable-artifact-member`, `portable-artifact-pointer`, `typed-artifact-pointer-alias`, `document-structure-artifact`, `claim-ledger-artifact`, `projection-source-support`, `projection-coverage-artifact`, `projection-coverage-entry`, `quality-report`, `ledger-quality-report-artifact`, `quality-check-catalog-artifact`, `blocked-write-diagnostic-artifact`. |
| `page-hash-invalid` | `page-projection`, `cross-source-projection` | `wiki-page`, `page-body`, `projection-coverage-artifact`. |
| `review-required` | `ledger-build`, `page-projection`, `cross-source-projection` | `source-statement`, `ledger-entry`, `atom-candidate`, `technical-atom`, `generated-page-claim`, `source-review-section`, `source-review-item`. |
| `audit-metric` | `ledger-build`, `page-projection`, `blocked-write`, `cross-source-projection` | `portable-artifact-set`, `quality-report`, `ledger-quality-report-artifact`, `quality-check-catalog-artifact`, `claim-ledger-artifact`, `source-profile`, `source-family-assignment`, `extractor-decision`, `extracted-unit`, `projection-coverage-artifact`, `blocked-write-diagnostic-artifact`. |

`ReviewWorkItem` stores these fields.

| ReviewWorkItem Field | Contract |
|---|---|
| `QualityFindingReason` | Controlled reason that produced the review item. |
| `QualityFindingSubject` | Structured subject that requires review. |
| `QualityFindingLocator` | Structured locator for the review item. |
| `ReviewReason` | Structured review reason. |

`QualityFindingSeverityPolicy` assigns one `QualityFindingSeverity` to each `QualityFindingReason`.
`QualityFindingSeverityPolicy` assigns `blocking` to `traceability-failure`, `coverage-gap`, `technical-atom-fidelity-failure`, `schema-invalid`, `controlled-vocabulary-invalid`, `canonical-order-invalid`, and `page-hash-invalid`.
`QualityFindingSeverityPolicy` assigns `warning` to `review-required`.
`QualityFindingSeverityPolicy` assigns `info` to `audit-metric`.
`QualityFindingReasonTaxonomy` uses source-neutral categories that correspond to domain object contracts.
`PortableArtifactSet` stores one `PortableArtifactSetId`.
`PortableArtifactSet` stores one `PortableArtifactSetFingerprint`.
`PortableArtifactSet` stores one `PortableArtifactMember` record for each child portable artifact.
`PortableArtifactSet` follows `CanonicalOrder`.
`PortableArtifactSet` does not embed child artifact bodies.
`PortableArtifactSet` does not list itself as a `PortableArtifactMember`.
`PortableArtifactMember` stores one `PortableArtifactKind`.
`PortableArtifactMember` does not use `PortableArtifactKind` `portable-artifact-set`.
`PortableArtifactMember` stores one target artifact id.
`PortableArtifactMember` stores one target artifact fingerprint.
`PortableArtifactMember` stores one `ArtifactFormat`.
`PortableArtifactPointer` stores one target artifact id.
`PortableArtifactPointer` stores one target artifact fingerprint.
`PortableArtifactPointer` resolves to one `PortableArtifactMember` in `PortableArtifactSet`.
`PortableArtifactPointer` resolves from that `PortableArtifactMember` to one child artifact.
`PortableArtifactPointer` target artifact fingerprint matches the resolved artifact fingerprint.
`TypedArtifactPointerAlias` names one target artifact type.
`PortableArtifact` exposes one typed artifact fingerprint field.
`PortableArtifact` does not expose a persisted field named `ArtifactFingerprint`.
Typed artifact fingerprint fields use the artifact domain type name.
`ProjectionCoveragePointer` uses `PortableArtifactPointer`.
`DocumentStructurePointer` uses `PortableArtifactPointer`.
`ClaimLedgerPointer` uses `PortableArtifactPointer`.
`LedgerQualityReportPointer` uses `PortableArtifactPointer`.
`QualityCheckCatalogPointer` uses `PortableArtifactPointer`.
`LedgerQualityReportArtifact` stores one `LedgerQualityReport`.
`LedgerQualityReportArtifact` stores one `LedgerQualityReportArtifactId`.
`LedgerQualityReportArtifact` stores one `LedgerQualityReportFingerprint`.
`LedgerQualityReportArtifact` follows `CanonicalOrder`.
`PortableArtifactSet` contains one `LedgerQualityReportArtifact` for each `LedgerQualityReportFingerprint`.
`BlockedWriteDiagnosticArtifact` stores one `BlockedWriteDiagnosticFingerprint`.
`ClaimLedgerArtifact` stores one `LedgerQualityReportPointer`.
`ProjectionCoverageArtifact` stores one `LedgerQualityReportPointer`.
`BlockedWriteDiagnosticArtifact` stores one `LedgerQualityReportPointer`.
`LedgerQualityReportPointer` stores one `LedgerQualityReportArtifactId`.
`LedgerQualityReportPointer` stores one `LedgerQualityReportFingerprint`.
`ClaimLedgerArtifact` does not embed `LedgerQualityReport`.
`ProjectionCoverageArtifact` does not embed `LedgerQualityReport`.
`BlockedWriteDiagnosticArtifact` does not embed `LedgerQualityReport`.
`QualityCheckCatalogArtifact` stores one `QualityCheckCatalog`.
`QualityCheckCatalogArtifact` stores one `QualityCheckCatalogArtifactId`.
`QualityCheckCatalogArtifact` stores one `QualityCheckCatalogFingerprint`.
`QualityCheckCatalogArtifact` stores `ReasonApplicabilityPolicy`.
`QualityCheckCatalogArtifact` stores `QualityFindingSeverityPolicy`.
`QualityCheckCatalogArtifact` follows `CanonicalOrder`.
`PortableArtifactSet` contains one `QualityCheckCatalogArtifact` for each `QualityCheckCatalogFingerprint`.
`LedgerQualityReport` references `QualityCheckCatalogArtifact`.
`LedgerQualityReport` does not embed `QualityCheckCatalogArtifact`.
`QualityCheckCatalog` stores one `QualityCheckDefinition` for each exact rule that creates `QualityFinding`.
`QualityCheckCatalog` stores one `QualityCheckId` for each `QualityCheckDefinition`.
`QualityCheckDefinition` stores one `QualityFindingReason`.
`QualityCheckDefinition` stores `AllowedQualityReportScopes`.
`QualityCheckDefinition` stores `AllowedQualityFindingSubjectKinds`.
`QualityCheckDefinition` stores one `QualityFindingSubjectField`.
`ReasonApplicabilityPolicy` stores one applicability row for each `QualityFindingReason`.
`ReasonApplicabilityPolicy` stores `AllowedQualityReportScopes` for each `QualityFindingReason`.
`ReasonApplicabilityPolicy` stores `AllowedQualityFindingSubjectKinds` for each `QualityFindingReason`.
`LedgerQualityReport` stores one `QualityReportScope`.
`LedgerQualityReport` stores one `QualityCheckCatalogPointer`.
`LedgerQualityReport` stores one `QualityFinding` for each flagged condition.
`LedgerQualityReport` stores one `QualityReportScope` for each `QualityFinding`.
`LedgerQualityReport` stores one `QualityCheckId` for each `QualityFinding`.
`LedgerQualityReport` stores one `QualityFindingSeverity` for each `QualityFinding`.
`LedgerQualityReport` stores one `QualityFindingReason` for each `QualityFinding`.
`LedgerQualityReport` stores one `QualityFindingSubject` for each `QualityFinding`.
`LedgerQualityReport` stores one `QualityFindingLocator` for each `QualityFinding`.
`LedgerQualityReport` flags `LedgerQualityReport` records without `QualityReportScope`.
`LedgerQualityReport` flags `LedgerQualityReport` records whose `QualityReportScope` is not in the controlled vocabulary.
`LedgerQualityReport` flags `PortableArtifactSet` records without `PortableArtifactSetId`.
`LedgerQualityReport` flags `PortableArtifactSet` records without `PortableArtifactSetFingerprint`.
`LedgerQualityReport` flags `PortableArtifactSet` records without `PortableArtifactMember` records.
`LedgerQualityReport` flags `PortableArtifactSet` records whose `PortableArtifactSetFingerprint` differs from canonical manifest contents.
`LedgerQualityReport` flags `PortableArtifactSet` records that do not follow `CanonicalOrder`.
`LedgerQualityReport` flags `PortableArtifactSet` records that embed child artifact bodies.
`LedgerQualityReport` flags `PortableArtifactSet` records that list themselves as `PortableArtifactMember` records.
`LedgerQualityReport` flags duplicate `PortableArtifactMember` records.
`LedgerQualityReport` flags `PortableArtifactMember` records without `PortableArtifactKind`.
`LedgerQualityReport` flags `PortableArtifactMember` records whose `PortableArtifactKind` is not in the controlled vocabulary.
`LedgerQualityReport` flags `PortableArtifactMember` records whose `PortableArtifactKind` is `portable-artifact-set`.
`LedgerQualityReport` flags `PortableArtifactMember` records without target artifact id.
`LedgerQualityReport` flags `PortableArtifactMember` records without target artifact fingerprint.
`LedgerQualityReport` flags `PortableArtifactMember` records without `ArtifactFormat`.
`LedgerQualityReport` flags `PortableArtifactMember` records whose target artifact does not resolve.
`LedgerQualityReport` flags `PortableArtifactMember` records whose target artifact fingerprint differs from the resolved child artifact.
`LedgerQualityReport` flags `PortableArtifactPointer` records without target artifact id.
`LedgerQualityReport` flags `PortableArtifactPointer` records without target artifact fingerprint.
`LedgerQualityReport` flags `PortableArtifactPointer` records that do not resolve to one `PortableArtifactMember` in `PortableArtifactSet`.
`LedgerQualityReport` flags `PortableArtifactPointer` records whose resolved `PortableArtifactMember` target artifact does not resolve.
`LedgerQualityReport` flags `PortableArtifactPointer` records whose target artifact fingerprint differs from the resolved artifact.
`LedgerQualityReport` flags `TypedArtifactPointerAlias` records whose target artifact type is ambiguous.
`LedgerQualityReport` flags `PortableArtifact` records without a typed artifact fingerprint field.
`LedgerQualityReport` flags `PortableArtifact` records with a persisted field named `ArtifactFingerprint`.
`LedgerQualityReport` flags `PortableArtifact` records whose typed artifact fingerprint field does not use the artifact domain type name.
`LedgerQualityReport` flags `LedgerQualityReportArtifact` records without `LedgerQualityReportArtifactId`.
`LedgerQualityReport` flags `LedgerQualityReportArtifact` records without `LedgerQualityReportFingerprint`.
`LedgerQualityReport` flags `LedgerQualityReportArtifact` records without `LedgerQualityReport`.
`LedgerQualityReport` flags `LedgerQualityReportArtifact` records whose `LedgerQualityReportFingerprint` differs from the canonical report contents.
`LedgerQualityReport` flags `LedgerQualityReportArtifact` records that do not follow `CanonicalOrder`.
`LedgerQualityReport` flags `BlockedWriteDiagnosticArtifact` records without `BlockedWriteDiagnosticFingerprint`.
`LedgerQualityReport` flags `BlockedWriteDiagnosticArtifact` records whose `BlockedWriteDiagnosticFingerprint` differs from the canonical diagnostic contents.
`LedgerQualityReport` flags `ClaimLedgerArtifact` records without `LedgerQualityReportPointer`.
`LedgerQualityReport` flags `ProjectionCoverageArtifact` records without `LedgerQualityReportPointer`.
`LedgerQualityReport` flags `BlockedWriteDiagnosticArtifact` records without `LedgerQualityReportPointer`.
`LedgerQualityReport` flags `ClaimLedgerArtifact` records that embed `LedgerQualityReport`.
`LedgerQualityReport` flags `ProjectionCoverageArtifact` records that embed `LedgerQualityReport`.
`LedgerQualityReport` flags `BlockedWriteDiagnosticArtifact` records that embed `LedgerQualityReport`.
`LedgerQualityReport` flags `LedgerQualityReportPointer` records without `LedgerQualityReportArtifactId`.
`LedgerQualityReport` flags `LedgerQualityReportPointer` records without `LedgerQualityReportFingerprint`.
`LedgerQualityReport` flags `LedgerQualityReportPointer` records that do not resolve to one `LedgerQualityReportArtifact`.
`LedgerQualityReport` flags `LedgerQualityReportPointer` records whose `LedgerQualityReportFingerprint` differs from the resolved `LedgerQualityReportArtifact`.
`LedgerQualityReport` flags `LedgerQualityReport` records without `QualityCheckCatalogPointer`.
`LedgerQualityReport` flags `LedgerQualityReport` records that embed `QualityCheckCatalogArtifact`.
`LedgerQualityReport` flags `QualityCheckCatalogPointer` records without `QualityCheckCatalogArtifactId`.
`LedgerQualityReport` flags `QualityCheckCatalogPointer` records without `QualityCheckCatalogFingerprint`.
`LedgerQualityReport` flags `QualityCheckCatalogPointer` records that do not resolve to one `QualityCheckCatalogArtifact`.
`LedgerQualityReport` flags `QualityCheckCatalogPointer` records whose `QualityCheckCatalogFingerprint` differs from the resolved `QualityCheckCatalogArtifact`.
`LedgerQualityReport` flags `QualityCheckCatalogArtifact` records without `QualityCheckCatalogArtifactId`.
`LedgerQualityReport` flags `QualityCheckCatalogArtifact` records without `QualityCheckCatalogFingerprint`.
`LedgerQualityReport` flags `QualityCheckCatalogArtifact` records without `QualityCheckCatalog`.
`LedgerQualityReport` flags `QualityCheckCatalogArtifact` records without `ReasonApplicabilityPolicy`.
`LedgerQualityReport` flags `QualityCheckCatalogArtifact` records without `QualityFindingSeverityPolicy`.
`LedgerQualityReport` flags `QualityCheckCatalogArtifact` records whose `QualityCheckCatalogFingerprint` differs from the canonical catalog and policy contents.
`LedgerQualityReport` flags `QualityCheckCatalogArtifact` records that do not follow `CanonicalOrder`.
`LedgerQualityReport` flags `QualityCheckCatalog` records with duplicate `QualityCheckId` values.
`LedgerQualityReport` flags `QualityFinding` records without `QualityCheckId`.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityCheckId` is not in the resolved `QualityCheckCatalogArtifact`.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityFindingReason` does not match `QualityCheckDefinition`.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityReportScope` is not allowed by `QualityCheckDefinition`.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityFindingSubjectKind` is not allowed by `QualityCheckDefinition`.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityFindingSubjectField` does not match `QualityCheckDefinition`.
`LedgerQualityReport` flags `QualityFinding` records without `QualityReportScope`.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityReportScope` differs from the owning report.
`LedgerQualityReport` flags `QualityFinding` records without `QualityFindingSeverity`.
`LedgerQualityReport` flags `QualityFinding` records without `QualityFindingReason`.
`LedgerQualityReport` flags `QualityFinding` records without `QualityFindingSubject`.
`LedgerQualityReport` flags `QualityFinding` records without `QualityFindingLocator`.
`LedgerQualityReport` flags `QualityFindingSubject` records without `QualityFindingSubjectKind`.
`LedgerQualityReport` flags `QualityFindingSubject` records whose `QualityFindingSubjectKind` is not in the controlled vocabulary.
`LedgerQualityReport` flags `QualityFindingSubject` records without `QualityFindingSubjectId`.
`LedgerQualityReport` flags `QualityFindingSubject` records without `QualityFindingSubjectField`.
`LedgerQualityReport` accepts `QualityFindingSubjectField` `whole-object` for every `QualityFindingSubjectKind`.
`LedgerQualityReport` flags `QualityFindingSubjectField` values other than `whole-object` that do not exist on the named subject kind.
`LedgerQualityReport` flags `QualityFindingLocator` records without `QualityFindingLocatorKind`.
`LedgerQualityReport` flags `QualityFindingLocator` records whose `QualityFindingLocatorKind` is not in the controlled vocabulary.
`LedgerQualityReport` flags `QualityFindingLocator` records that lack fields required by `QualityFindingLocatorKind`.
`LedgerQualityReport` flags `QualityFindingLocator` records that do not resolve in the `PortableArtifactSet`.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityFindingSeverity` is not in the controlled vocabulary.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityFindingReason` is not in the controlled vocabulary.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityFindingSeverity` does not match `QualityFindingSeverityPolicy`.
`LedgerQualityReport` flags `QualityCheckDefinition` records without `QualityCheckId`.
`LedgerQualityReport` flags `QualityCheckDefinition` records without `QualityFindingReason`.
`LedgerQualityReport` flags `QualityCheckDefinition` records without `AllowedQualityReportScopes`.
`LedgerQualityReport` flags `QualityCheckDefinition` records without `AllowedQualityFindingSubjectKinds`.
`LedgerQualityReport` flags `QualityCheckDefinition` records without `QualityFindingSubjectField`.
`LedgerQualityReport` flags `QualityCheckDefinition` records whose `QualityFindingReason` is not in the controlled vocabulary.
`LedgerQualityReport` flags `QualityCheckDefinition` records whose `QualityFindingSubjectField` is neither `whole-object` nor a field on every allowed subject kind.
`LedgerQualityReport` flags `QualityCheckDefinition` records whose `AllowedQualityReportScopes` are not allowed by `ReasonApplicabilityPolicy`.
`LedgerQualityReport` flags `QualityCheckDefinition` records whose `AllowedQualityFindingSubjectKinds` are not allowed by `ReasonApplicabilityPolicy`.
`LedgerQualityReport` flags `QualityFindingReason` values missing from `ReasonApplicabilityPolicy`.
`LedgerQualityReport` flags `ReasonApplicabilityPolicy` rows with values outside `QualityReportScope`.
`LedgerQualityReport` flags `ReasonApplicabilityPolicy` rows with values outside `QualityFindingSubjectKind`.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityReportScope` is not allowed by `ReasonApplicabilityPolicy`.
`LedgerQualityReport` flags `QualityFinding` records whose `QualityFindingSubjectKind` is not allowed by `ReasonApplicabilityPolicy`.
`LedgerQualityReport` flags `PageWriteDecision` `block-authoritative-write` without `BlockedWriteDiagnosticArtifact`.
`LedgerQualityReport` flags `BlockedWriteDiagnosticArtifact` records whose `PageWriteDecision` is not `block-authoritative-write`.
`LedgerQualityReport` flags `BlockedWriteDiagnosticArtifact` records whose `LedgerQualityReportPointer` does not resolve to `QualityReportScope` `blocked-write`.
`LedgerQualityReport` flags `BlockedWriteDiagnosticArtifact` records without `ClaimLedgerPointer`.
`LedgerQualityReport` flags `BlockedWriteDiagnosticArtifact` records without `WikiPageLocator`.
`LedgerQualityReport` flags `BlockedWriteDiagnosticArtifact` records that contain `WikiPage`.
`LedgerQualityReport` flags `BlockedWriteDiagnosticArtifact` records that contain `ProjectionCoverageArtifact`.
`LedgerQualityReport` flags `GeneratedPageClaim` units with no `SelectedLedgerEntryIds`.
`LedgerQualityReport` flags wiki pages without `ProjectionCoveragePointer`.
`LedgerQualityReport` flags `ProjectionCoverageArtifact` records without `ProjectionSourceSupportSet`.
`LedgerQualityReport` flags `ProjectionCoverageArtifact` records for `SourceWikiPage` with more than one `ProjectionSourceSupport` record.
`LedgerQualityReport` flags `ProjectionCoverageArtifact` records for `SourceWikiPage` with zero `ProjectionSourceSupport` records.
`LedgerQualityReport` flags `ProjectionCoverageArtifact` records for `CrossSourceWikiPage` with fewer than two `ProjectionSourceSupport` records.
`LedgerQualityReport` flags `ProjectionSourceSupport` records without `SourceHash`.
`LedgerQualityReport` flags `ProjectionSourceSupport` records without `SourceLocator`.
`LedgerQualityReport` flags `ProjectionSourceSupport` records without `ClaimLedgerPointer`.
`LedgerQualityReport` flags `ProjectionSourceSupport` records whose `ClaimLedgerPointer` does not resolve.
`LedgerQualityReport` flags `ProjectionSourceSupport` records without `DocumentStructurePointer`.
`LedgerQualityReport` flags `ProjectionSourceSupport` records whose `DocumentStructurePointer` does not resolve.
`LedgerQualityReport` flags `ProjectionSourceSupport` records without a `SourceCitation` whose `SourceLocator` resolves to the record.
`LedgerQualityReport` flags `ProjectionSourceSupportSet` values that do not follow `CanonicalOrder`.
`LedgerQualityReport` flags `ProjectionCoverageArtifact` records whose `PageBodyHash` mismatches.
`LedgerQualityReport` flags `PageBody` content that displays `InternalSupportId` values.
`LedgerQualityReport` flags `SourceCitation` records without `SourceCitationLabel`.
`LedgerQualityReport` flags `SourceCitation` records without `SourceLocator`.
`LedgerQualityReport` flags `SourceCitation` records whose `SourceLocator` does not resolve to exactly one `ProjectionSourceSupport`.
`LedgerQualityReport` flags `SourceWikiPage` records whose page order does not follow `SourceStructureSpine`.
`LedgerQualityReport` flags `SourceStructureSection` records that do not follow `SourceOrder`.
`LedgerQualityReport` flags `SynthesisSection` records that precede `SourceStructureSection` records.
`LedgerQualityReport` flags `SourceReviewSection` records that precede `SourceStructureSection` records.
`LedgerQualityReport` flags `SourceReviewSection` records that precede existing `SynthesisSection` records.
`LedgerQualityReport` flags `SourceReviewItem` records without `SourceCitation`.
`LedgerQualityReport` flags `SourceReviewItem` records without `ReviewReason`.
`LedgerQualityReport` flags `SourceReviewItem` records without `ProjectionCoverageEntry` records.
`LedgerQualityReport` flags `SourceReviewItem` records whose `ProjectionCoverageEntry` unit kind is not `source-review-item`.
`LedgerQualityReport` flags `SourceReviewItem` records whose `LedgerEntryStatus` is not `needs-review`.
`LedgerQualityReport` flags `DispositionCount` records without `ProjectionCoverageEntry` records.
`LedgerQualityReport` flags `DispositionCount` records whose `ProjectionCoverageEntry` unit kind is not `disposition-count`.
`LedgerQualityReport` flags `DispositionCount` records whose `DispositionCountValue` does not match extracted-unit dispositions.
`LedgerQualityReport` flags `SynthesisSection` `GeneratedPageClaim` units without `ProjectionCoverageEntry` records.
`LedgerQualityReport` flags `ProjectionCoverageEntry` records without `PageTextRange`.
`LedgerQualityReport` flags `ProjectionCoverageEntry` records whose `SelectedLedgerEntryIds` do not resolve to `ProjectionSourceSupportSet`.
`LedgerQualityReport` flags `ProjectionCoverageEntry` records whose `TechnicalAtomId` does not resolve to `ProjectionSourceSupportSet`.
`LedgerQualityReport` flags `ProjectionCoverageEntry` records whose `LedgerEntryId` does not resolve to `ProjectionSourceSupportSet`.
`LedgerQualityReport` flags `ProjectionCoverageEntry` records whose `CrossSourceRelationshipId` does not resolve to a `CrossSourceRelationship`.
`LedgerQualityReport` flags `ProjectionCoverageEntry` records with unit kind `source-review-item` and no `LedgerEntryId`.
`LedgerQualityReport` flags `ProjectionCoverageEntry` records with unit kind `disposition-count` and no `ExtractedUnitDisposition`.
`LedgerQualityReport` flags `ProjectionCoverageEntry` records with unit kind `cross-source-relationship` and no `CrossSourceRelationshipId`.
`LedgerQualityReport` flags `SourceBackedPosition` records whose `SelectedLedgerEntryIds` do not resolve to exactly one `ProjectionSourceSupport`.
`LedgerQualityReport` flags `CrossSourceRelationship` records without `ProjectionCoverageEntry` records.
`LedgerQualityReport` flags `CrossSourceRelationship` records whose `ProjectionCoverageEntry` unit kind is not `cross-source-relationship`.
`LedgerQualityReport` flags `CrossSourceRelationship` records whose `CrossSourceRelationshipKind` is not in the controlled vocabulary.
`LedgerQualityReport` flags `CrossSourceRelationship` records with fewer than two `RelatedProjectionCoverageEntryIds`.
`LedgerQualityReport` flags `CrossSourceRelationship` records whose `RelatedProjectionCoverageEntryIds` do not resolve to `SourceBackedPosition` entries.
`LedgerQualityReport` flags `CrossSourceRelationship` records whose `RelatedProjectionCoverageEntryIds` resolve to fewer than two `ProjectionSourceSupport` records.
`LedgerQualityReport` flags `GeneratedPageClaim` units without `ProjectionCoverageEntry` records.
`LedgerQualityReport` flags `GeneratedPageClaim` units that select entries with `LedgerEntryStatus` `needs-review` or `rejected`.
`LedgerQualityReport` flags `GeneratedPageClaim` units whose `SelectedLedgerEntryIds` include entries from both positions in a `conflicts-with` `CrossSourceRelationship`.
`LedgerQualityReport` flags accepted `TechnicalAtom` records without `RenderedTechnicalAtomBlock` records.
`LedgerQualityReport` flags `RenderedTechnicalAtomBlock` units without `TechnicalAtomId`.
`LedgerQualityReport` flags `RenderedTechnicalAtomBlock` units with multiple `ProjectionCoverageEntry` records.
`LedgerQualityReport` flags `RenderedTechnicalAtomBlock` records that render entries with `LedgerEntryStatus` `needs-review` or `rejected`.
`LedgerQualityReport` flags `RenderedTechnicalAtomBlock` records outside the matching `SourceStructureSection`.
`LedgerQualityReport` flags `RenderedTechnicalAtomBlock` records whose order does not follow `SourceOrder`.
`LedgerQualityReport` flags `RenderedTechnicalAtomBlock` records without `SourceEquivalentPayload`.
`LedgerQualityReport` flags `GeneratedPageClaim` units that explain a `TechnicalAtom` when the matching `RenderedTechnicalAtomBlock` is absent.
`LedgerQualityReport` flags `GeneratedPageClaim` units whose `ProjectionCoverageEntry` unit kind is not `generated-page-claim`.
`LedgerQualityReport` flags broad-only citations when narrower locators exist.
`LedgerQualityReport` flags technical atoms whose payload lacks required structure.
`LedgerQualityReport` flags atom candidates that fail the active atom schema set.
`LedgerQualityReport` summarizes rejected candidates by reason and evidence range.
`LedgerQualityReport` reports extractor decision counts by capability and status.
`LedgerQualityReport` flags extracted units without one decision per active extractor capability.
`LedgerQualityReport` flags candidate-produced decisions without atom candidate ids.
`LedgerQualityReport` flags abstained decisions without abstain reason.
`LedgerQualityReport` flags abstain reasons with unknown reason kinds.
`LedgerQualityReport` flags abstain reasons with missing typed fields.
`LedgerQualityReport` flags ranker scores outside `RankerScoreRange`.
`LedgerQualityReport` flags unknown `CalibrationBucket` values.
`LedgerQualityReport` flags `CalibrationBucket` values that do not match `CalibrationThresholds`.
`LedgerQualityReport` flags active extractor capabilities without `CalibrationThresholds`.
`LedgerQualityReport` flags source profiles whose assignment confidence is below the reporting threshold.
`LedgerQualityReport` flags extracted units with no disposition.
`LedgerQualityReport` reports counts for accepted, structural, needs-review, rejected, and non-claim units.

### Verification Targets

Tests use synthetic sources and renamed-domain variants.
Tests can include real regression examples.
Real regression examples cannot be the only proof.

The history source test includes names, dates, events, cause, and coincidence.
The coding source test includes code blocks, idioms, best practices, anti-patterns, and formulas.
The rules-reference source test includes rules, tables, procedures, classes, and settings.

Tests prove extractor capabilities are ranked from extracted-unit feature signals.
Tests prove schema input supplies the active extractor capability set.
Tests prove every extracted unit has one extractor decision per active extractor capability.
Tests prove schema input supplies the active abstain reason policy.
Tests prove schema input supplies the active `CalibrationPolicy`.
Tests prove ranker scores use `RankerScoreRange`.
Tests prove `CalibrationBucket` uses a controlled vocabulary.
Tests prove calibration policy defines `CalibrationThresholds` per active extractor capability.
Tests prove calibration policy rejects source-specific thresholds.
Tests prove equal feature signal values produce equal `CalibrationBucket` values.
Tests prove quality report flags ranker scores outside `RankerScoreRange`.
Tests prove quality report flags unknown `CalibrationBucket` values.
Tests prove quality report flags `CalibrationBucket` values that do not match `CalibrationThresholds`.
Tests prove abstain reason kinds use a controlled vocabulary.
Tests prove abstain reason fields use typed values.
Tests prove abstain reason policy validates required fields by reason kind.
Tests prove renamed-domain source variants produce the same abstain reason kinds.
Tests prove feature signal kinds use a controlled vocabulary.
Tests prove feature signal values use typed values.
Tests prove feature signal policy rejects source-specific feature signal kinds.
Tests prove feature signal policy rejects lexical-only detectors as acceptance rules.
Tests prove renamed-domain source variants produce the same feature signal kinds.
Tests prove feature signals cannot accept atom candidates without atom schema validation.
Tests prove extracted unit profiles store measured feature signals only.
Tests prove extracted unit profiles do not store ranker scores.
Tests prove atom candidates store materialized payload data for one extractor capability.
Tests prove atom candidates store source-neutral ranker fields.
Tests prove atom candidates do not store prompts, transcripts, or raw ranker internals.
Tests prove pure abstentions become extractor decisions only.
Tests prove abstained extractor decisions carry abstain reason.
Tests prove candidate-produced extractor decisions carry atom candidate id.
Tests prove atom candidates require payload or review reason.
Tests prove claim ledger artifacts include extractor decisions.
Tests prove accepted atom candidates become ledger entries.
Tests prove rejected atom candidates become rejected candidates.
Tests prove schema input supplies the active atom schema set.
Tests prove atom schema definitions declare required fields by technical atom kind.
Tests prove valid atom candidates become ledger entries.
Tests prove invalid atom candidates do not become ledger entries.
Tests prove atom validator rejects candidates that fail the active atom schema set.
Tests prove table atoms preserve raw table text.
Tests prove parsed table atoms preserve row order, column order, and cell coordinates.
Tests prove partially-parsed table atoms keep raw table text and review reason.
Tests prove unparsed table atoms keep raw table text and review reason.
Tests prove code atoms preserve exact code text and whitespace.
Tests prove detected language tags carry language confidence.
Tests prove code AST output is optional.
Tests prove code AST output is not source authority.
Tests prove rule atoms preserve exact rule text.
Tests prove rule candidates use source-neutral linguistic, structural, and semantic-role categories.
Tests prove lexical cues alone cannot accept rule atoms.
Tests prove rule schema decides whether a rule candidate becomes a rule atom.
Tests prove rule atoms can support linked claim-like entries.
Tests prove requirements become rule atoms with required rule force.
Tests prove rule exceptions stay in rule exception fields when they modify one rule.
Tests prove standalone exceptions can become rule atoms or relationship entries.
Tests prove procedure atoms are separate from rule atoms.
Tests prove procedure atoms preserve exact procedure text.
Tests prove procedure steps preserve source order.
Tests prove rule atoms can reference procedure steps.
Tests prove worked example atoms preserve exact example text.
Tests prove worked example atoms preserve setup, input, operation, output, and explanation.
Tests prove worked example atoms can reference other technical atoms.
Tests prove symbolic formulas can use equation or prose surface forms.
Tests prove procedural formulas can use equation or prose surface forms.
Tests prove formula atoms retain exact source text when parsing fails.
Tests prove formula-derived ledger entries reference the formula atom.
Tests prove formula atoms remain preserved when derived entries are absent.
Tests prove quotation entries preserve exact source wording.
Tests prove quotation-derived entries reference the quotation entry.
Tests prove entries become needs-review when exact required wording cannot be preserved.
Tests prove confidence policy maps source-neutral signals to extraction confidence.
Tests prove confidence policy does not score source truth.
Tests prove low-confidence claim-like entries become needs-review.
Tests prove exact-preservation atoms can be usable with medium confidence.
Tests prove claim-like entries require subject, predicate, object, polarity, claim force, condition scope, temporal scope, and spatial scope.
Tests prove conditions and exceptions are separate from claim force.
Tests prove asserted negative propositions use negative polarity.
Tests prove prohibitions over positive propositions use forbidden claim force and affirmative polarity.
Tests prove possible claim force means source-stated possibility.
Tests prove extraction uncertainty uses confidence and status, not possible claim force.
Tests prove temporal scope preserves exact source wording.
Tests prove relative temporal scope has anchor entry ids or unresolved confidence.
Tests prove temporal normalization is optional.
Tests prove spatial scope preserves exact source wording.
Tests prove relative spatial scope has anchor entry ids or unresolved confidence.
Tests prove spatial normalization is optional.
Tests prove normalized text alone cannot make a complete claim-like entry.
Tests prove compound source statements split into atomic ledger entries.
Tests prove source statements retain the original source text for split entries.
Tests prove split entries keep temporal, causal, conditional, and sequential links.
Tests prove split entries become needs-review when required local context is missing.
Tests prove every extracted unit has exactly one disposition.
Tests prove structural units become structure nodes, not non-claim units.
Tests prove subject-matterless residue can become non-claim units.
Tests prove `SourceWikiPage` projection uses `DocumentStructure` and `ClaimLedger` records.
Tests prove `CrossSourceWikiPage` projection uses two or more `ProjectionSourceSupport` records.
Tests prove `SourceWikiPage` layout follows `SourceStructureSpine`.
Tests prove `SourceStructureSpine` derives from `DocumentStructure`.
Tests prove `SourceStructureSection` order follows `SourceOrder`.
Tests prove `SynthesisSection` records follow `SourceStructureSection` records.
Tests prove `SourceReviewSection` records follow `SourceStructureSection` records.
Tests prove `SourceReviewSection` records follow `SynthesisSection` records when a `SynthesisSection` exists.
Tests prove `SourceReviewSection` records include `SourceReviewItem` records for `needs-review` entries.
Tests prove `SourceReviewItem` records include `SourceCitation` and `ReviewReason`.
Tests prove `SourceReviewSection` records include `DispositionCount` records for `rejected` and `non-claim` units.
Tests prove `SynthesisSection` `GeneratedPageClaim` units have `ProjectionCoverageEntry` records.
Tests prove `SourceReviewItem` records have `ProjectionCoverageEntry` records with unit kind `source-review-item`.
Tests prove `DispositionCount` records have `ProjectionCoverageEntry` records with unit kind `disposition-count`.
Tests prove `WikiPageMetadata` carries `ProjectionCoveragePointer`.
Tests prove `ProjectionCoveragePointer` uses `PortableArtifactPointer`.
Tests prove `ProjectionCoveragePointer` stores `ProjectionCoverageArtifactId`.
Tests prove `ProjectionCoveragePointer` stores `ProjectionCoverageFingerprint`.
Tests prove `PageBody` carries `SourceCitation` records.
Tests prove `PageBody` displays `SourceCitationLabel` values.
Tests prove `PageBody` does not display `InternalSupportId` values.
Tests prove `PageBody` does not contain `ProjectionCoveragePointer`.
Tests prove `ProjectionCoverageArtifact` records map `PageBody` text to `ProjectionCoverageEntry` records.
Tests prove `ProjectionCoverageArtifact` records store `ProjectionCoverageFingerprint`.
Tests prove `ProjectionCoverageArtifact` records store `ProjectionSourceSupportSet`.
Tests prove `ProjectionCoverageArtifact` records for `SourceWikiPage` use exactly one `ProjectionSourceSupport` record.
Tests prove `ProjectionCoverageArtifact` records for `CrossSourceWikiPage` use two or more `ProjectionSourceSupport` records.
Tests prove `ProjectionSourceSupportSet` follows `CanonicalOrder`.
Tests prove `ProjectionCoverageArtifact` records store `InternalSupportId` values.
Tests prove `ProjectionSourceSupport` records store `DocumentStructurePointer`.
Tests prove `ProjectionSourceSupport` records store `ClaimLedgerPointer`.
Tests prove `ClaimLedgerPointer` uses `PortableArtifactPointer`.
Tests prove `ClaimLedgerPointer` resolves to one `ClaimLedgerArtifact`.
Tests prove `DocumentStructurePointer` uses `PortableArtifactPointer`.
Tests prove `DocumentStructurePointer` resolves to one `DocumentStructureArtifact`.
Tests prove source citation labels stay source-facing across renamed-domain variants.
Tests prove `SourceCitation` records resolve to exactly one `ProjectionSourceSupport`.
Tests prove `ProjectionCoverageEntry` records use one `ProjectionCoverageUnit`.
Tests prove each `GeneratedPageClaim` has one `ProjectionCoverageEntry`.
Tests prove one paragraph with multiple `GeneratedPageClaim` units has multiple `ProjectionCoverageEntry` records.
Tests prove conflicting `SourceBackedPosition` records render as separate `GeneratedPageClaim` units.
Tests prove `SourceBackedPosition` records resolve to exactly one `ProjectionSourceSupport`.
Tests prove each `CrossSourceRelationship` has one `ProjectionCoverageEntry`.
Tests prove each `CrossSourceRelationship` maps to one `CrossSourceRelationshipId`.
Tests prove `CrossSourceRelationship` records use `CrossSourceRelationshipKind` values.
Tests prove `CrossSourceRelationship` records relate two or more `SourceBackedPosition` records.
Tests prove each `RenderedTechnicalAtomBlock` maps to one `TechnicalAtomId`.
Tests prove each `SourceReviewItem` maps to one `LedgerEntryId`.
Tests prove each `DispositionCount` maps to one `ExtractedUnitDisposition`.
Tests prove accepted `TechnicalAtom` records render as `RenderedTechnicalAtomBlock` records.
Tests prove `RenderedTechnicalAtomBlock` records appear in the matching `SourceStructureSection`.
Tests prove `RenderedTechnicalAtomBlock` order follows `SourceOrder`.
Tests prove `RenderedTechnicalAtomBlock` records render `SourceEquivalentPayload`.
Tests prove prose that interprets a `TechnicalAtom` has separate `GeneratedPageClaim` coverage.
Tests prove each `ProjectionCoverageUnitKind` uses a distinct unit contract.
Tests prove quality report flags `WikiPage` records without `ProjectionCoveragePointer`.
Tests prove `LedgerQualityReportArtifact` stores one `LedgerQualityReport`.
Tests prove `LedgerQualityReportArtifact` stores one `LedgerQualityReportArtifactId`.
Tests prove `LedgerQualityReportArtifact` stores one `LedgerQualityReportFingerprint`.
Tests prove `LedgerQualityReportArtifact` follows `CanonicalOrder`.
Tests prove `PortableArtifactSet` stores one `PortableArtifactSetId`.
Tests prove `PortableArtifactSet` stores one `PortableArtifactSetFingerprint`.
Tests prove `PortableArtifactSet` stores one `PortableArtifactMember` record for each child portable artifact.
Tests prove `PortableArtifactSet` follows `CanonicalOrder`.
Tests prove `PortableArtifactSet` does not embed child artifact bodies.
Tests prove `PortableArtifactSet` does not list itself as a `PortableArtifactMember`.
Tests prove changed child artifact membership produces a new `PortableArtifactSetFingerprint`.
Tests prove `PortableArtifactMember` records store `PortableArtifactKind`, target artifact id, target artifact fingerprint, and `ArtifactFormat`.
Tests prove `PortableArtifactMember` records do not use `PortableArtifactKind` `portable-artifact-set`.
Tests prove `ArtifactManifestBuilder` returns the same `PortableArtifactSet` for the same portable artifact descriptors.
Tests prove `ArtifactManifestBuilder` performs no I/O.
Tests prove `ArtifactManifestOutputPort` receives `PortableArtifactSet` records.
Tests prove `ArtifactManifestStoreAdapter` persists `PortableArtifactSet` records.
Tests prove `PortableArtifactSet` contains one `LedgerQualityReportArtifact` for each `LedgerQualityReportFingerprint`.
Tests prove `PortableArtifactPointer` stores one target artifact id.
Tests prove `PortableArtifactPointer` stores one target artifact fingerprint.
Tests prove `PortableArtifactPointer` resolves to one `PortableArtifactMember` in `PortableArtifactSet`.
Tests prove `PortableArtifactPointer` resolves from `PortableArtifactMember` to one child artifact.
Tests prove `PortableArtifactPointer` rejects target artifact fingerprint mismatches.
Tests prove `TypedArtifactPointerAlias` names one target artifact type.
Tests prove typed artifact fingerprints use `ArtifactFingerprint` rules.
Tests prove typed artifact fingerprints exclude their own typed fingerprint fields.
Tests prove typed artifact fingerprints exclude artifact id fields whose deterministic input is that fingerprint.
Tests prove typed artifact fingerprint fields use the artifact domain type name.
Tests prove portable artifacts expose typed artifact fingerprint fields.
Tests prove portable artifacts do not expose persisted fields named `ArtifactFingerprint`.
Tests prove `ClaimLedgerArtifact` records store `LedgerQualityReportPointer`.
Tests prove `ProjectionCoverageArtifact` records store `LedgerQualityReportPointer`.
Tests prove `BlockedWriteDiagnosticArtifact` records store `LedgerQualityReportPointer`.
Tests prove `LedgerQualityReportPointer` uses `PortableArtifactPointer`.
Tests prove `ClaimLedgerArtifact` records do not embed `LedgerQualityReport`.
Tests prove `ProjectionCoverageArtifact` records do not embed `LedgerQualityReport`.
Tests prove `BlockedWriteDiagnosticArtifact` records do not embed `LedgerQualityReport`.
Tests prove `LedgerQualityReportPointer` resolves to one `LedgerQualityReportArtifact`.
Tests prove `LedgerQualityReportPointer` rejects report fingerprint mismatches.
Tests prove changed report contents produce a new `LedgerQualityReportFingerprint`.
Tests prove `LedgerQualityReport` has one `QualityReportScope`.
Tests prove `QualityReportScope` uses `ledger-build`, `page-projection`, `blocked-write`, or `cross-source-projection`.
Tests prove `ledger-build` checks source-scoped ledger artifacts before page projection.
Tests prove `page-projection` checks one `SourceWikiPage` and its `ProjectionCoverageArtifact`.
Tests prove `blocked-write` checks one `BlockedWriteDiagnosticArtifact`.
Tests prove `cross-source-projection` checks one `CrossSourceWikiPage` and its cross-source relationships.
Tests prove `LedgerQualityReport` stores one `QualityFinding` for each flagged condition.
Tests prove each `QualityFinding` has one `QualityCheckId`.
Tests prove each `QualityCheckId` resolves to one `QualityCheckDefinition`.
Tests prove `QualityCheckId` uses source-neutral domain vocabulary.
Tests prove renamed-domain variants use the same `QualityCheckId` for the same exact rule.
Tests prove each `QualityFinding` has one `QualityReportScope`.
Tests prove each `QualityFinding` uses the owning `LedgerQualityReport` `QualityReportScope`.
Tests prove renamed-domain variants use the same `QualityReportScope` for the same report operation.
Tests prove each `QualityFinding` has one `QualityFindingSeverity`.
Tests prove each `QualityFinding` has one `QualityFindingReason`.
Tests prove each `QualityFinding` has one `QualityFindingSubject`.
Tests prove each `QualityFinding` has one `QualityFindingLocator`.
Tests prove each `QualityFindingSubject` has one `QualityFindingSubjectKind`.
Tests prove each `QualityFindingSubject` has one `QualityFindingSubjectId`.
Tests prove each `QualityFindingSubject` has one `QualityFindingSubjectField`.
Tests prove `QualityFindingSubjectField` uses `whole-object` for object-scoped findings.
Tests prove `QualityFindingSubjectKind` values match the subject kind table.
Tests prove `QualityFindingSubjectField` values other than `whole-object` match domain fields for the named subject kind.
Tests prove each `QualityFindingLocator` has one `QualityFindingLocatorKind`.
Tests prove `QualityFindingLocatorKind` values match the locator kind table.
Tests prove each `QualityFindingLocatorKind` has its required locator fields.
Tests prove each `QualityFindingLocator` resolves in the `PortableArtifactSet`.
Tests prove renamed-domain variants use the same `QualityFindingSubjectKind` and `QualityFindingLocatorKind` for the same domain contract violation.
Tests prove `QualityFindingSeverity` uses `blocking`, `warning`, or `info`.
Tests prove `QualityFindingReasonTaxonomy` contains `traceability-failure`, `coverage-gap`, `technical-atom-fidelity-failure`, `schema-invalid`, `controlled-vocabulary-invalid`, `canonical-order-invalid`, `page-hash-invalid`, `review-required`, and `audit-metric`.
Tests prove `QualityFindingSeverityPolicy` maps each `QualityFindingReason` to one `QualityFindingSeverity`.
Tests prove `QualityFindingSeverityPolicy` assigns `blocking` to `traceability-failure`, `coverage-gap`, `technical-atom-fidelity-failure`, `schema-invalid`, `controlled-vocabulary-invalid`, `canonical-order-invalid`, and `page-hash-invalid`.
Tests prove `QualityFindingSeverityPolicy` assigns `warning` to `review-required`.
Tests prove `QualityFindingSeverityPolicy` assigns `info` to `audit-metric`.
Tests prove synthetic sources with renamed domain nouns produce the same `QualityFindingReason` for the same domain contract violation.
Tests prove `QualityCheckCatalog` stores one `QualityCheckDefinition` for each exact rule that creates `QualityFinding`.
Tests prove `QualityCheckCatalogArtifact` stores one `QualityCheckCatalog`.
Tests prove `QualityCheckCatalogArtifact` stores one `QualityCheckCatalogArtifactId`.
Tests prove `QualityCheckCatalogArtifact` stores one `QualityCheckCatalogFingerprint`.
Tests prove `QualityCheckCatalogArtifact` stores `ReasonApplicabilityPolicy`.
Tests prove `QualityCheckCatalogArtifact` stores `QualityFindingSeverityPolicy`.
Tests prove `QualityCheckCatalogArtifact` follows `CanonicalOrder`.
Tests prove `QualityCheckCatalogFingerprint` changes when a `QualityCheckDefinition`, `ReasonApplicabilityPolicy`, or `QualityFindingSeverityPolicy` changes.
Tests prove `PortableArtifactSet` contains one `QualityCheckCatalogArtifact` for each `QualityCheckCatalogFingerprint`.
Tests prove `LedgerQualityReport` records with the same `QualityCheckCatalogFingerprint` reference the same `QualityCheckCatalogArtifact`.
Tests prove `LedgerQualityReport` does not embed `QualityCheckCatalogArtifact`.
Tests prove changed catalog or policy contents produce a new `QualityCheckCatalogFingerprint`.
Tests prove `LedgerQualityReport` stores one `QualityCheckCatalogPointer`.
Tests prove `QualityCheckCatalogPointer` uses `PortableArtifactPointer`.
Tests prove `QualityCheckCatalogPointer` resolves to one `QualityCheckCatalogArtifact`.
Tests prove `QualityCheckCatalogPointer` rejects catalog fingerprint mismatches.
Tests prove each `QualityFinding` resolves its `QualityCheckId` through the owning `LedgerQualityReport` `QualityCheckCatalogPointer`.
Tests prove each `QualityCheckDefinition` has one `QualityCheckId`.
Tests prove each `QualityCheckDefinition` has one `QualityFindingReason`.
Tests prove each `QualityCheckDefinition` has `AllowedQualityReportScopes`.
Tests prove each `QualityCheckDefinition` has `AllowedQualityFindingSubjectKinds`.
Tests prove each `QualityCheckDefinition` has one `QualityFindingSubjectField`.
Tests prove each `QualityFinding` uses the `QualityFindingReason` from its `QualityCheckDefinition`.
Tests prove each `QualityFinding` uses a `QualityReportScope` allowed by its `QualityCheckDefinition`.
Tests prove each `QualityFinding` uses a `QualityFindingSubjectKind` allowed by its `QualityCheckDefinition`.
Tests prove each `QualityFinding` uses the `QualityFindingSubjectField` from its `QualityCheckDefinition`.
Tests prove `QualityCheckDefinition` scope and subject values are allowed by `ReasonApplicabilityPolicy`.
Tests prove `ReasonApplicabilityPolicy` stores one applicability row for each `QualityFindingReason`.
Tests prove `ReasonApplicabilityPolicy` stores `AllowedQualityReportScopes` for each `QualityFindingReason`.
Tests prove `ReasonApplicabilityPolicy` stores `AllowedQualityFindingSubjectKinds` for each `QualityFindingReason`.
Tests prove `ReasonApplicabilityPolicy` values match the applicability table.
Tests prove each `QualityFinding` uses a `QualityReportScope` allowed by `ReasonApplicabilityPolicy`.
Tests prove each `QualityFinding` uses a `QualityFindingSubjectKind` allowed by `ReasonApplicabilityPolicy`.
Tests prove renamed-domain variants use the same `ReasonApplicabilityPolicy` result for the same domain contract violation.
Tests prove `WriteBoundary` returns `block-authoritative-write` when `LedgerQualityReport` contains a `blocking` finding.
Tests prove `WriteBoundary` returns `write-with-review-work` when `LedgerQualityReport` contains a `warning` finding and no `blocking` finding.
Tests prove `WriteBoundary` returns `write-authoritative-page` when `LedgerQualityReport` contains only `info` findings.
Tests prove `WriteBoundary` returns `write-authoritative-page` when `LedgerQualityReport` contains no `QualityFinding` records.
Tests prove `WriteBoundary` creates `BlockedWriteDiagnosticArtifact` when `PageWriteDecision` is `block-authoritative-write`.
Tests prove `BlockedWriteDiagnosticArtifact` stores `PageWriteDecision` `block-authoritative-write`.
Tests prove `BlockedWriteDiagnosticArtifact` stores `BlockedWriteDiagnosticFingerprint`.
Tests prove changed blocked write diagnostic contents produce a new `BlockedWriteDiagnosticFingerprint`.
Tests prove `BlockedWriteDiagnosticArtifact` stores `LedgerQualityReportPointer` that resolves to `QualityReportScope` `blocked-write`.
Tests prove `BlockedWriteDiagnosticArtifact` stores `ClaimLedgerPointer`.
Tests prove `BlockedWriteDiagnosticArtifact` stores `WikiPageLocator`.
Tests prove `BlockedWriteDiagnosticArtifact` stores no `WikiPage`.
Tests prove `BlockedWriteDiagnosticArtifact` stores no `ProjectionCoverageArtifact`.
Tests prove `DiagnosticOutputPort` receives `BlockedWriteDiagnosticArtifact`.
Tests prove `DiagnosticStoreAdapter` persists `BlockedWriteDiagnosticArtifact`.
Tests prove `QualityReportStoreAdapter` persists `LedgerQualityReportArtifact`.
Tests prove `WikiStoreAdapter` writes no `WikiPage` or `ProjectionCoverageArtifact` when `PageWriteDecision` is `block-authoritative-write`.
Tests prove `WikiStoreAdapter` writes `WikiPage`, `ProjectionCoverageArtifact`, and `ReviewWorkItem` records when `PageWriteDecision` is `write-with-review-work`.
Tests prove `WikiStoreAdapter` writes `WikiPage` and `ProjectionCoverageArtifact` when `PageWriteDecision` is `write-authoritative-page`.
Tests prove `ReviewWorkItem` records derive from warning `QualityFinding` records.
Tests prove quality report flags `LedgerQualityReport` records without `QualityReportScope`.
Tests prove quality report flags `LedgerQualityReport` records whose `QualityReportScope` is not in the controlled vocabulary.
Tests prove quality report flags `LedgerQualityReportArtifact` records without `LedgerQualityReportArtifactId`.
Tests prove quality report flags `LedgerQualityReportArtifact` records without `LedgerQualityReportFingerprint`.
Tests prove quality report flags `LedgerQualityReportArtifact` records without `LedgerQualityReport`.
Tests prove quality report flags `LedgerQualityReportArtifact` records whose `LedgerQualityReportFingerprint` differs from the canonical report contents.
Tests prove quality report flags `LedgerQualityReportArtifact` records that do not follow `CanonicalOrder`.
Tests prove quality report flags `PortableArtifactSet` records without `PortableArtifactSetId`.
Tests prove quality report flags `PortableArtifactSet` records without `PortableArtifactSetFingerprint`.
Tests prove quality report flags `PortableArtifactSet` records without `PortableArtifactMember` records.
Tests prove quality report flags `PortableArtifactSet` records whose `PortableArtifactSetFingerprint` differs from canonical manifest contents.
Tests prove quality report flags `PortableArtifactSet` records that do not follow `CanonicalOrder`.
Tests prove quality report flags `PortableArtifactSet` records that embed child artifact bodies.
Tests prove quality report flags `PortableArtifactSet` records that list themselves as `PortableArtifactMember` records.
Tests prove quality report flags `ClaimLedgerArtifact` records without `LedgerQualityReportPointer`.
Tests prove quality report flags `ProjectionCoverageArtifact` records without `LedgerQualityReportPointer`.
Tests prove quality report flags `BlockedWriteDiagnosticArtifact` records without `LedgerQualityReportPointer`.
Tests prove quality report flags `ClaimLedgerArtifact` records that embed `LedgerQualityReport`.
Tests prove quality report flags `ProjectionCoverageArtifact` records that embed `LedgerQualityReport`.
Tests prove quality report flags `BlockedWriteDiagnosticArtifact` records that embed `LedgerQualityReport`.
Tests prove quality report flags `PortableArtifactPointer` records without target artifact id.
Tests prove quality report flags `PortableArtifactPointer` records without target artifact fingerprint.
Tests prove quality report flags `PortableArtifactMember` records with duplicate target artifact ids and fingerprints.
Tests prove quality report flags `PortableArtifactMember` records without `PortableArtifactKind`.
Tests prove quality report flags `PortableArtifactMember` records whose `PortableArtifactKind` is not in the controlled vocabulary.
Tests prove quality report flags `PortableArtifactMember` records whose `PortableArtifactKind` is `portable-artifact-set`.
Tests prove quality report flags `PortableArtifactMember` records without target artifact id.
Tests prove quality report flags `PortableArtifactMember` records without target artifact fingerprint.
Tests prove quality report flags `PortableArtifactMember` records without `ArtifactFormat`.
Tests prove quality report flags `PortableArtifactMember` records whose target artifact does not resolve.
Tests prove quality report flags `PortableArtifactMember` records whose target artifact fingerprint differs from the resolved child artifact.
Tests prove quality report flags `PortableArtifactPointer` records that do not resolve to one `PortableArtifactMember` in `PortableArtifactSet`.
Tests prove quality report flags `PortableArtifactPointer` records whose resolved `PortableArtifactMember` target artifact does not resolve.
Tests prove quality report flags `PortableArtifactPointer` records whose target artifact fingerprint differs from the resolved artifact.
Tests prove quality report flags `TypedArtifactPointerAlias` records whose target artifact type is ambiguous.
Tests prove quality report flags portable artifacts without typed artifact fingerprint fields.
Tests prove quality report flags portable artifacts with persisted fields named `ArtifactFingerprint`.
Tests prove quality report flags portable artifacts whose typed artifact fingerprint field does not use the artifact domain type name.
Tests prove quality report flags `LedgerQualityReportPointer` records without `LedgerQualityReportArtifactId`.
Tests prove quality report flags `LedgerQualityReportPointer` records without `LedgerQualityReportFingerprint`.
Tests prove quality report flags `LedgerQualityReportPointer` records that do not resolve to one `LedgerQualityReportArtifact`.
Tests prove quality report flags `LedgerQualityReportPointer` records whose `LedgerQualityReportFingerprint` differs from the resolved `LedgerQualityReportArtifact`.
Tests prove quality report flags `LedgerQualityReport` records without `QualityCheckCatalogPointer`.
Tests prove quality report flags `LedgerQualityReport` records that embed `QualityCheckCatalogArtifact`.
Tests prove quality report flags `QualityCheckCatalogPointer` records without `QualityCheckCatalogArtifactId`.
Tests prove quality report flags `QualityCheckCatalogPointer` records without `QualityCheckCatalogFingerprint`.
Tests prove quality report flags `QualityCheckCatalogPointer` records that do not resolve to one `QualityCheckCatalogArtifact`.
Tests prove quality report flags `QualityCheckCatalogPointer` records whose `QualityCheckCatalogFingerprint` differs from the resolved `QualityCheckCatalogArtifact`.
Tests prove quality report flags `QualityCheckCatalogArtifact` records without `QualityCheckCatalogArtifactId`.
Tests prove quality report flags `QualityCheckCatalogArtifact` records without `QualityCheckCatalogFingerprint`.
Tests prove quality report flags `QualityCheckCatalogArtifact` records without `QualityCheckCatalog`.
Tests prove quality report flags `QualityCheckCatalogArtifact` records without `ReasonApplicabilityPolicy`.
Tests prove quality report flags `QualityCheckCatalogArtifact` records without `QualityFindingSeverityPolicy`.
Tests prove quality report flags `QualityCheckCatalogArtifact` records whose `QualityCheckCatalogFingerprint` differs from the canonical catalog and policy contents.
Tests prove quality report flags `QualityCheckCatalogArtifact` records that do not follow `CanonicalOrder`.
Tests prove quality report flags `QualityCheckCatalog` records with duplicate `QualityCheckId` values.
Tests prove quality report flags `QualityFinding` records without `QualityCheckId`.
Tests prove quality report flags `QualityFinding` records whose `QualityCheckId` is not in the resolved `QualityCheckCatalogArtifact`.
Tests prove quality report flags `QualityFinding` records whose `QualityFindingReason` does not match `QualityCheckDefinition`.
Tests prove quality report flags `QualityFinding` records whose `QualityReportScope` is not allowed by `QualityCheckDefinition`.
Tests prove quality report flags `QualityFinding` records whose `QualityFindingSubjectKind` is not allowed by `QualityCheckDefinition`.
Tests prove quality report flags `QualityFinding` records whose `QualityFindingSubjectField` does not match `QualityCheckDefinition`.
Tests prove quality report flags `QualityFinding` records without `QualityReportScope`.
Tests prove quality report flags `QualityFinding` records whose `QualityReportScope` differs from the owning report.
Tests prove quality report flags `QualityFinding` records without `QualityFindingSeverity`.
Tests prove quality report flags `QualityFinding` records without `QualityFindingReason`.
Tests prove quality report flags `QualityFinding` records without `QualityFindingSubject`.
Tests prove quality report flags `QualityFinding` records without `QualityFindingLocator`.
Tests prove quality report flags `QualityFindingSubject` records without `QualityFindingSubjectKind`.
Tests prove quality report flags `QualityFindingSubject` records whose `QualityFindingSubjectKind` is not in the controlled vocabulary.
Tests prove quality report flags `QualityFindingSubject` records without `QualityFindingSubjectId`.
Tests prove quality report flags `QualityFindingSubject` records without `QualityFindingSubjectField`.
Tests prove quality report accepts `QualityFindingSubjectField` `whole-object` for every `QualityFindingSubjectKind`.
Tests prove quality report flags `QualityFindingSubjectField` values other than `whole-object` that do not exist on the named subject kind.
Tests prove quality report flags `QualityFindingLocator` records without `QualityFindingLocatorKind`.
Tests prove quality report flags `QualityFindingLocator` records whose `QualityFindingLocatorKind` is not in the controlled vocabulary.
Tests prove quality report flags `QualityFindingLocator` records that lack fields required by `QualityFindingLocatorKind`.
Tests prove quality report flags `QualityFindingLocator` records that do not resolve in the `PortableArtifactSet`.
Tests prove quality report flags `QualityFinding` records whose `QualityFindingSeverity` is not in the controlled vocabulary.
Tests prove quality report flags `QualityFinding` records whose `QualityFindingReason` is not in the controlled vocabulary.
Tests prove quality report flags `QualityFinding` records whose `QualityFindingSeverity` does not match `QualityFindingSeverityPolicy`.
Tests prove quality report flags `QualityCheckDefinition` records without `QualityCheckId`.
Tests prove quality report flags `QualityCheckDefinition` records without `QualityFindingReason`.
Tests prove quality report flags `QualityCheckDefinition` records without `AllowedQualityReportScopes`.
Tests prove quality report flags `QualityCheckDefinition` records without `AllowedQualityFindingSubjectKinds`.
Tests prove quality report flags `QualityCheckDefinition` records without `QualityFindingSubjectField`.
Tests prove quality report flags `QualityCheckDefinition` records whose `QualityFindingReason` is not in the controlled vocabulary.
Tests prove quality report flags `QualityCheckDefinition` records whose `QualityFindingSubjectField` is neither `whole-object` nor a field on every allowed subject kind.
Tests prove quality report flags `QualityCheckDefinition` records whose `AllowedQualityReportScopes` are not allowed by `ReasonApplicabilityPolicy`.
Tests prove quality report flags `QualityCheckDefinition` records whose `AllowedQualityFindingSubjectKinds` are not allowed by `ReasonApplicabilityPolicy`.
Tests prove quality report flags `QualityFindingReason` values missing from `ReasonApplicabilityPolicy`.
Tests prove quality report flags `ReasonApplicabilityPolicy` rows with values outside `QualityReportScope`.
Tests prove quality report flags `ReasonApplicabilityPolicy` rows with values outside `QualityFindingSubjectKind`.
Tests prove quality report flags `QualityFinding` records whose `QualityReportScope` is not allowed by `ReasonApplicabilityPolicy`.
Tests prove quality report flags `QualityFinding` records whose `QualityFindingSubjectKind` is not allowed by `ReasonApplicabilityPolicy`.
Tests prove quality report flags `PageWriteDecision` `block-authoritative-write` without `BlockedWriteDiagnosticArtifact`.
Tests prove quality report flags `BlockedWriteDiagnosticArtifact` records whose `PageWriteDecision` is not `block-authoritative-write`.
Tests prove quality report flags `BlockedWriteDiagnosticArtifact` records without `BlockedWriteDiagnosticFingerprint`.
Tests prove quality report flags `BlockedWriteDiagnosticArtifact` records whose `BlockedWriteDiagnosticFingerprint` differs from canonical diagnostic contents.
Tests prove quality report flags `BlockedWriteDiagnosticArtifact` records whose `LedgerQualityReportPointer` does not resolve to `QualityReportScope` `blocked-write`.
Tests prove quality report flags `BlockedWriteDiagnosticArtifact` records without `ClaimLedgerPointer`.
Tests prove quality report flags `BlockedWriteDiagnosticArtifact` records without `WikiPageLocator`.
Tests prove quality report flags `BlockedWriteDiagnosticArtifact` records that contain `WikiPage`.
Tests prove quality report flags `BlockedWriteDiagnosticArtifact` records that contain `ProjectionCoverageArtifact`.
Tests prove quality report flags `ProjectionCoverageArtifact` records without `ProjectionSourceSupportSet`.
Tests prove quality report flags `ProjectionCoverageArtifact` records for `SourceWikiPage` without exactly one `ProjectionSourceSupport` record.
Tests prove quality report flags `ProjectionCoverageArtifact` records for `CrossSourceWikiPage` with fewer than two `ProjectionSourceSupport` records.
Tests prove quality report flags `ProjectionSourceSupport` records with missing required fields.
Tests prove quality report flags `ProjectionSourceSupport` records without `ClaimLedgerPointer`.
Tests prove quality report flags `ProjectionSourceSupport` records whose `ClaimLedgerPointer` does not resolve.
Tests prove quality report flags `ProjectionSourceSupport` records without `DocumentStructurePointer`.
Tests prove quality report flags `ProjectionSourceSupport` records whose `DocumentStructurePointer` does not resolve.
Tests prove quality report flags `ProjectionSourceSupport` records without a resolving `SourceCitation`.
Tests prove quality report flags `ProjectionSourceSupportSet` values that do not follow `CanonicalOrder`.
Tests prove quality report flags `ProjectionCoverageArtifact` records whose `PageBodyHash` mismatches.
Tests prove quality report flags `PageBody` content that displays `InternalSupportId` values.
Tests prove quality report flags `SourceCitation` records whose `SourceLocator` does not resolve to exactly one `ProjectionSourceSupport`.
Tests prove quality report flags `SourceWikiPage` records whose page order does not follow `SourceStructureSpine`.
Tests prove quality report flags `SynthesisSection` `GeneratedPageClaim` units without `ProjectionCoverageEntry` records.
Tests prove quality report flags `SourceReviewItem` records without `SourceCitation`.
Tests prove quality report flags `SourceReviewItem` records without `ReviewReason`.
Tests prove quality report flags `SourceReviewItem` records without `ProjectionCoverageEntry` records.
Tests prove quality report flags `SourceReviewItem` records whose `ProjectionCoverageEntry` unit kind is not `source-review-item`.
Tests prove quality report flags `DispositionCount` records without `ProjectionCoverageEntry` records.
Tests prove quality report flags `DispositionCount` records whose `ProjectionCoverageEntry` unit kind is not `disposition-count`.
Tests prove quality report flags `DispositionCount` records whose `DispositionCountValue` does not match extracted-unit dispositions.
Tests prove quality report flags `ProjectionCoverageEntry` records with unit kind `source-review-item` and no `LedgerEntryId`.
Tests prove quality report flags `ProjectionCoverageEntry` records with unit kind `disposition-count` and no `ExtractedUnitDisposition`.
Tests prove quality report flags `ProjectionCoverageEntry` records with unit kind `cross-source-relationship` and no `CrossSourceRelationshipId`.
Tests prove quality report flags `ProjectionCoverageEntry` records whose `SelectedLedgerEntryIds`, `TechnicalAtomId`, or `LedgerEntryId` do not resolve to `ProjectionSourceSupportSet`.
Tests prove quality report flags `SourceBackedPosition` records whose `SelectedLedgerEntryIds` do not resolve to exactly one `ProjectionSourceSupport`.
Tests prove quality report flags `CrossSourceRelationship` records without `ProjectionCoverageEntry` records.
Tests prove quality report flags `CrossSourceRelationship` records whose `ProjectionCoverageEntry` unit kind is not `cross-source-relationship`.
Tests prove quality report flags `CrossSourceRelationship` records whose `CrossSourceRelationshipKind` is not in the controlled vocabulary.
Tests prove quality report flags `CrossSourceRelationship` records with fewer than two `RelatedProjectionCoverageEntryIds`.
Tests prove quality report flags `CrossSourceRelationship` records whose `RelatedProjectionCoverageEntryIds` do not resolve to `SourceBackedPosition` entries.
Tests prove quality report flags `CrossSourceRelationship` records whose `RelatedProjectionCoverageEntryIds` resolve to fewer than two `ProjectionSourceSupport` records.
Tests prove quality report flags `GeneratedPageClaim` units whose `SelectedLedgerEntryIds` include entries from both positions in a `conflicts-with` `CrossSourceRelationship`.
Tests prove quality report flags `GeneratedPageClaim` units whose `ProjectionCoverageEntry` unit kind is not `generated-page-claim`.
Tests prove quality report flags `GeneratedPageClaim` units that select entries with `LedgerEntryStatus` `needs-review` or `rejected`.
Tests prove quality report flags accepted `TechnicalAtom` records without `RenderedTechnicalAtomBlock` records.
Tests prove quality report flags `RenderedTechnicalAtomBlock` records that render entries with `LedgerEntryStatus` `needs-review` or `rejected`.
Tests prove quality report flags `RenderedTechnicalAtomBlock` records whose order does not follow `SourceOrder`.
Tests prove `SourceFamilyAssignment` is derived after atom validation.
Tests prove `SourceFamilyAssignment` does not change which atom kinds can be extracted.
Tests prove that the same source text under two filenames produces the same entry kinds and statuses.
Tests prove that two sources with the same table structure produce the same table atom shape.
Tests prove that `DomainModule` functions return the same output for the same input.
Tests prove that `DomainModule` functions do not perform I/O.

### Reference Models

The design follows W3C PROV for provenance and evidence traceability.
The design follows RDF-style subject-predicate-object graphs for relationship records.
The design follows SKOS-style concept schemes for concept organization.
The design follows CIDOC CRM-style event modeling for history sources.
The design follows source-statement grouping for PROV-backed atomic splitting.
The design follows W3C tabular data for table payload fidelity.
The design follows FrameNet-style roles for event and rule participants.
The design follows calibrated multi-label classification for source profile labels.
The design follows facet analysis for source-neutral concept facets.
The design follows deontic logic for required, permitted, forbidden, and recommended claim force.
The design follows rule modeling practice for conditions and exceptions as separate scope fields.

### Alignment With LLM-Wiki

This design keeps raw sources immutable.
This design keeps the wiki layer generated and disposable.
This design makes `WikiPage` records maintained projections of durable source-derived ledgers.
This design keeps `index.md` and `log.md` as navigation and history artifacts.
This design improves ingest, query, and lint by giving each operation a verifiable claim ledger.
