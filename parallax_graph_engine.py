import json
import os
import parallax_model

class ParallaxGraphEngine:
    def __init__(self):
        self.engine_config = parallax_model.PARALLAX_KNOWLEDGE_ENGINE
        self.triples = []
        self.contradictions = []
        
    def add_triple(self, subject, relation, obj, layer, source, confidence=0.85):
        """
        Pievieno un validē jaunu zināšanu grafa trijnieku.
        Saglabā pretrunas atsevišķos mezglos, nevis tās izdzēš.
        """
        triple = {
            "subject": subject,
            "relation": relation,
            "object": obj,
            "layer": layer,
            "source": source,
            "confidence": confidence
        }
        
        # Pārbaudām pretrunas (ja ir tāds pats subjekts un relācija, bet cits objekts)
        existing = [t for t in self.triples if t["subject"] == subject and t["relation"] == relation]
        if existing and existing[0]["object"] != obj:
            contradiction_record = {
                "new_incoming": triple,
                "existing_node": existing[0],
                "status": "Preserved Conflict Node"
            }
            self.contradictions.append(contradiction_record)
            print(f"⚠️ Konstatēta pretruna saglabāta mezglam: {subject} -> {relation}")
            
        self.triples.append(triple)

    def calculate_mapped_percentage(self, total_capacity_nodes=500):
        """
        Aprēķina platformas faktisko mērāmo 'mapped %' 
        balstoties uz unikālajām entitātēm un starp-slāņu izomorfismiem.
        """
        unique_entities = set()
        cross_layer_isomorphisms = 0
        
        for t in self.triples:
            unique_entities.add(t["subject"])
            unique_entities.add(t["object"])
            if t["relation"] in ["ISOMORPHIC_TO", "SHARES_TOPOLOGY_WITH", "FRACTAL_MAPPING"]:
                cross_layer_isomorphisms += 1
                
        # Aprēķina formula (izomorfisma saitēm ir lielāks svars matricas sintēzē)
        raw_score = (len(unique_entities) + (cross_layer_isomorphisms * 2.5)) / total_capacity_nodes * 100
        return min(round(raw_score, 2), 100.0)

    def export_graph_state(self):
        """Eksportē grafa stāvokli, lai to varētu publicēt myparallax.org vai sūtīt uz Telegram."""
        return {
            "total_triples": len(self.triples),
            "total_contradictions": len(self.contradictions),
            "current_mapped_percentage": self.calculate_mapped_percentage(),
            "triples": self.triples,
            "contradictions": self.contradictions
        }

if __name__ == "__main__":
    print("Inicē Parallax Graph Engine...")
    graph_engine = ParallaxGraphEngine()
    
    # Testam pievienojam pāris parauga trijniekus atbilstoši ontoloģijai
    graph_engine.add_triple("Göbekli_Tepe", "BUILT_BEFORE", "11600_BP", "module_1_lost_engineering", "X_Stream_Grok", 0.9)
    graph_engine.add_triple("Megalithic_Grid", "ISOMORPHIC_TO", "Neural_Network_Topology", "cosmic_isomorphism", "Research_Corpus", 0.95)
    
    print(f"Pašreizējais Mapped %: {graph_engine.calculate_mapped_percentage()}%")