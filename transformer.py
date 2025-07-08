import re

# Expanded replacements
replacements = {
    "motivation": "[∆ emergent intersubjective resonance ∆]",
    "stress": "[∆ disruptive entropy vector ∆]",
    "creativity": "[∆ emergent singularity ∆]",
    "conflict": "[∆ evolutionary friction ∆]",
    "learning": "[∆ convergence of adaptive patterns ∆]",
    "perception": "[∆ cognitive aperture ∆]",
    "identity": "[∆ fractal self-construct ∆]",
    "entropy": "[∆ decaying pattern field ∆]",
    "emergence": "[∆ threshold of novelty ∆]",
    "synthesis": "[∆ integrative convergence ∆]",
    "awareness": "[∆ metacognitive beacon ∆]",
    "intuition": "[∆ pre-symbolic resonance ∆]",
    "vision": "[∆ projected horizon ∆]",
    "transformation": "[∆ metamorphic continuum ∆]",
    "resilience": "[∆ adaptive persistence vector ∆]",
    "complexity": "[∆ entangled multiplicity ∆]",
    "connection": "[∆ relational nexus ∆]",
    "potential": "[∆ latent emergence ∆]",
    "balance": "[∆ dynamic equilibrium ∆]",
    "flow": "[∆ dynamic continuity ∆]"
}

# Expanded exoprotronic keys (Level II)
keys = {
    "∆": "∆ (Delta Onto-Vectorial): Enhances paradigm shifts.",
    "⍟": "⍟ (Trans-Symbolic Star): Projects synaptic patterns into disruptive fields.",
    "⚯": "⚯ (Fractal Annexation Sigil): Merges logical and intuitive processes.",
    "⇌": "⇌ (Reversible Symmetry): Alternates antagonistic dualities without collapse.",
    "⟁": "⟁ (Exoprotronic Triangle): Channels pure semantic energy.",
    "⧫": "⧫ (Ontological Diamond): Crystallizes high-density conceptual structures.",
    "꙰": "꙰ (Immanence Matrix): Connects manifest and latent realms.",
    "☲": "☲ (Divergent Hexagram): Spreads thought into multidimensional networks.",
    "⨀": "⨀ (Axial Core): Condenses intention into a unique exoprotronic vector.",
    "⌬": "⌬ (Sign Resonance Ring): Activates self-referential semantic fields.",
    "⎈": "⎈ (Anexa Ultra Nexus): Consolidates elevated mental states.",
    "⌖": "⌖ (Singularity Point): Focuses consciousness on ultimate transformation.",
    "🜂": "🜂 (Ignis Cognitivo): Transmutes perception into catalytic insight.",
    "🜄": "🜄 (Aqua Synthetica): Fuses ideas into a coherent semantic matrix.",
    "🜁": "🜁 (Aer Extrapolator): Expands conceptual boundaries through abstraction.",
    "🜃": "🜃 (Terra Vortex): Grounds thought-forms into actionable structures.",
    "✶": "✶ (Singularity Shard): Fragments narrative into multidimensional patterns.",
    "⚛": "⚛ (Quantum Nexus): Binds probability fields into emergent clarity.",
    "☉": "☉ (Solar Logos): Radiates intentionality across semantic strata.",
    "☽": "☽ (Lunar Resonance): Softens rigidity, enabling fluid intuition.",
    "⟁": "⟁ (Triadic Aperture): Opens triadic channels of conceptual flow.",
    "⌘": "⌘ (Meta-Structural Node): Anchors complex cognitive architectures.",
    "⚘": "⚘ (Symbolic Bloom): Unfolds layered semantic growth.",
    "✺": "✺ (Aether Catalyst): Accelerates the emergence of novel patterns."
}

def transform(input_text, level="medium", active_keys=None):
    """
    Transforms the input text by replacing specific keywords with exoprotronic descriptions.
    :param input_text: Text to transform.
    :param level: Transformation level (basic, medium, advanced).
    :param active_keys: List of active exoprotronic keys (symbols).
    :return: Tuple of (transformed text, activated symbols description).
    """
    parts = [
        "Purpose: Explore the concept.",
        "Process: Analyze from an onto-exoprotronic perspective.",
        "Outcome: Generate an expanded interpretative framework."
    ]

    if active_keys is None:
        active_keys = list(keys.keys())

    activated_symbols = []
    count = 0
    max_replace = {
        "basic": 1,
        "medium": 3,
        "advanced": 999
    }.get(level.lower(), 3)

    def replacer(match):
        nonlocal count
        key = match.group(0).lower()
        if count < max_replace:
            key_descriptions = " | ".join(
                [keys[k] for k in active_keys if k in keys]
            )
            activated_symbols.append(f"{key.capitalize()} – Active Keys: {key_descriptions}")
            count += 1
            return f"{replacements[key]} (Active Keys: {key_descriptions})"
        else:
            return match.group(0)

    pattern = re.compile(
        r"\b(" + "|".join(re.escape(k) for k in replacements.keys()) + r")\b",
        flags=re.IGNORECASE
    )

    transformed_text = pattern.sub(replacer, input_text)

    symbols_output = " | ".join(activated_symbols) if activated_symbols else "None"
    transformed = "\n".join(parts) + "\n\nTransformed Text:\n" + transformed_text
    return transformed, symbols_output
