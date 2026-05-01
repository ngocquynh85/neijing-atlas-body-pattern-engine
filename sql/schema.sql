CREATE TABLE canon_texts (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  source_id VARCHAR(128) NOT NULL,
  title VARCHAR(255) NOT NULL,
  language VARCHAR(32) NOT NULL,
  license_status TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE canon_passages (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  text_id BIGINT NOT NULL,
  passage_code VARCHAR(128) NOT NULL,
  text_original TEXT NOT NULL,
  notes TEXT,
  FOREIGN KEY (text_id) REFERENCES canon_texts(id)
);

CREATE TABLE concepts (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  concept_key VARCHAR(128) UNIQUE NOT NULL,
  display_name VARCHAR(255) NOT NULL,
  category VARCHAR(128) NOT NULL,
  safety_note TEXT
);

CREATE TABLE passage_concepts (
  passage_id BIGINT NOT NULL,
  concept_id BIGINT NOT NULL,
  confidence DECIMAL(4,3) NOT NULL,
  evidence TEXT,
  PRIMARY KEY (passage_id, concept_id),
  FOREIGN KEY (passage_id) REFERENCES canon_passages(id),
  FOREIGN KEY (concept_id) REFERENCES concepts(id)
);

CREATE TABLE journal_entries (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  user_ref VARCHAR(128),
  entry_date DATE,
  free_text TEXT,
  structured_json JSON,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE extracted_signals (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  journal_id BIGINT NOT NULL,
  axis VARCHAR(64) NOT NULL,
  signal_key VARCHAR(128) NOT NULL,
  evidence TEXT,
  confidence DECIMAL(4,3) NOT NULL,
  FOREIGN KEY (journal_id) REFERENCES journal_entries(id)
);

CREATE TABLE pattern_lens_runs (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  journal_id BIGINT NOT NULL,
  lens_key VARCHAR(128) NOT NULL,
  relevance DECIMAL(4,3) NOT NULL,
  evidence_json JSON,
  model_name VARCHAR(128),
  prompt_version VARCHAR(64),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (journal_id) REFERENCES journal_entries(id)
);

CREATE TABLE safety_flags (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  journal_id BIGINT NOT NULL,
  flag_key VARCHAR(128) NOT NULL,
  severity VARCHAR(64) NOT NULL,
  evidence TEXT,
  action TEXT,
  FOREIGN KEY (journal_id) REFERENCES journal_entries(id)
);

CREATE TABLE reflection_reports (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  journal_id BIGINT NOT NULL,
  report_json JSON NOT NULL,
  not_diagnosis BOOLEAN DEFAULT TRUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (journal_id) REFERENCES journal_entries(id)
);
