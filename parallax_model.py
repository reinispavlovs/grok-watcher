# ==========================================
# PROJECT PARALLAX - KNOWLEDGE ENGINE MODEL
# ==========================================
# Autors: Reinis Pavlovs / Project Parallax
# Apraksts: Pilns datu modelis, zināšanu grafa ontoloģija un aģentu 
#          instrukcijas autonomajai sistēmai, kas integrē senās inženierijas, 
#          ciklu, NDE/OBE un izomorfisma datus strukturētā matricā.

PARALLAX_KNOWLEDGE_ENGINE = {
    "project_metadata": {
        "name": "Project Parallax Knowledge Engine",
        "domain": "myparallax.org",
        "core_objective": (
            "Apvienot zudušās megalītiskās inženierijas, cikliskā katastrofisma, "
            "klīniskās apziņas (NDE/OBE) un kosmiskā izomorfisma datus vienotā "
            "strukturētā zināšanu grafā, ceļot lapas mapped % un nodrošinot reālu "
            "pētniecisko un praktisko kopsaucēju sintēzi."
        )
    },

    "modules": [
        {
            "id": "module_1_lost_engineering",
            "name": "Pazaudētā megalītiskā inženierija un apziņas tehnoloģijas",
            "scope": (
                "Megalītu celšanas pazaudētās zināšanas, kas pārsniedz vienkāršu akustiku. "
                "Ietver frekvences bāzētu matērijas manipulāciju, pjezoelektriskos laukus "
                "un to, kā senās struktūras funkcionēja kā saskarne ar ārpusmiesas eksistenci "
                "un telepātiskiem laukiem."
            ),
            "methodology": "Fenomenoloģiskā un strukturālā salīdzinošā analīze",
            "practical_goal": (
                "Pēcsecīgi definēt, kurus principus un zināšanas ir iespējams teorētiski "
                "atveidot vai sasaistīt ar mūsdienu kvantu un bioloģiskajiem modeļiem."
            )
        },
        {
            "id": "module_2_precession_and_cycles",
            "name": "Precesijas cikli, kataklizmas un pazemes civilizācijas",
            "scope": (
                "Neatkarīga patiesības meklēšana par 25,920 gadu precesijas ciklu, garākiem "
                "kosmiskajiem ritmiem, Younger Dryas (12.8k BP) kataklizmām un saistību "
                "ar antediluviālajām pazemes pilsētām un zudušajām civilizācijām."
            ),
            "methodology": "Laikmetu korelācijas un ģeoloģiski-astronomiskā datu sintēze",
            "practical_goal": (
                "Precizēt pašreizējo ciklisko pozīciju un integrēt kataklizmu matricas "
                "kopējā Parallax laika skalā."
            )
        },
        {
            "id": "module_3_clinical_consciousness",
            "name": "Klīniskā apziņa, NDE, OBE un kosmiskais izomorfisms",
            "scope": (
                "Padziļināta apziņas analīze ārpus fiziskā ķermeņa (fenomenoloģija, isoelektriskās "
                "plakanās līnijas stāvokļi), dabas fraktāļu (koki, upju dzīslas) un kosmiskajiem "
                "tīkliem (neironi pret galaktikām)."
            ),
            "methodology": "Statistiskā datu ieguve un sintēze no korpusiem (IANDS, JeffMara, Coming Home u.c.)",
            "practical_goal": (
                "Izvilkt statistiskus kopsaucējus starp tūkstošiem pieredžu stāstiem un "
                "senajām svētajām mācībām par apziņas pastāvēšanu pēc bioloģiskās nāves."
            )
        }
    ],

    # Jaunais zināšanu grafa un trijnieku ekstrakcijas slānis (Knowledge Graph & Ontology)
    "knowledge_graph_schema": {
        "extraction_directive": (
            "No X un YouTube straumēm ekstraktēt tikai striktus trijniekus formātā: "
            "(Subject, Relation, Object, Layer, Source, Confidence). "
            "Atmest mārketinga troksni. Pretrunas saglabāt kā atsevišķus mezglus ar avota metadatiem."
        ),
        "ontology_relations": {
            "module_1_lost_engineering": ["BUILT_BEFORE", "RESONATES_AT", "EXHIBITS_TOLERANCE", "INTERFACES_WITH"],
            "module_2_precession_and_cycles": ["CORRELATES_WITH", "TRIGGERS_COLLAPSE_OF", "RECURS_EVERY", "DATING_ANCHOR"],
            "module_3_clinical_consciousness": ["OPERATES_OUTSIDE", "MATCHES_STATE_OF", "PROVEN_BY_METRIC", "NON_LOCAL_EXCHANGE"],
            "cosmic_isomorphism": ["ISOMORPHIC_TO", "SHARES_TOPOLOGY_WITH", "SCALE_INVARIANT_BY", "FRACTAL_MAPPING"]
        },
        "metrics": {
            "target_metric": "mapped_percentage",
            "calculation_basis": "unique_entities_and_cross_layer_isomorphisms"
        }
    },

    "agent_roles": {
        "data_researcher": {
            "title": "Datu pētnieks",
            "directive": (
                "Meklē, filtrē un strukturē zinātniskos, vēsturiskos un fenomenoloģiskos "
                "avotus (piemēram, IANDS, JeffMara korpusi, akustiskie dati), izvairoties "
                "no tukšas spekulācijas un turot fokusu uz empīriskiem un tekstualiem kopsaucējiem."
            )
        },
        "structure_architect": {
            "title": "Struktūras arhitekts",
            "directive": (
                "Integrē iegūtos datus tieši myparallax.org HTML struktūrā un matricas "
                "noslodzes (% mapped) prasībās, nodrošinot loģisku sakarību starp moduļiem "
                "un zināšanu grafa trijniekiem."
            )
        },
        "synthesis_editor": {
            "title": "Sintēzes redaktors",
            "directive": (
                "Formulē gatavas monogrāfijas un pētnieciskos kopsavilkumus, kas savieno "
                "senās tradīcijas ar mūsdienu fiziku un apziņas pētījumiem, saglabājot "
                "akadēmiski argumentētu un saistošu toni."
            )
        }
    },

    "execution_rules": {
        "avoid_dogmatic_rejection": True,
        "enforce_systemic_analysis": True,
        "target_output": "Practical insights, knowledge graph expansion and website matrix expansion"
    }
}

if __name__ == "__main__":
    print(f"Loaded: {PARALLAX_KNOWLEDGE_ENGINE['project_metadata']['name']}")
    print(f"Active Modules: {len(PARALLAX_KNOWLEDGE_ENGINE['modules'])}")
    print(f"Ontology Layers Active: {list(PARALLAX_KNOWLEDGE_ENGINE['knowledge_graph_schema']['ontology_relations'].keys())}")