--  ==============================================================================================

CREATE TABLE "RC1" (
    "RC1TDOC" TEXT NOT NULL,
    "RC1NDOC" TEXT NOT NULL,
    "RC1NOM" TEXT NOT NULL,
    "RC1APE" TEXT NOT NULL,
    "RC1FNAC" DATE,
    PRIMARY KEY("RC1TDOC", "RC1NDOC")
)
CREATE INDEX "RC101" ON "RC1" (
	"RC1TDOC",
	"RC1NDOC"
)

CREATE TABLE "RC1a" (
    "RC1TDOC" TEXT NOT NULL,
    "RC1NDOC" TEXT NOT NULL,
    "RC1PW" TEXT NOT NULL,
    "RC1STAT" TEXT NOT NULL,
    PRIMARY KEY("RC1TDOC", "RC1NDOC"),
    FOREIGN KEY("RC1TDOC", "RC1NDOC") REFERENCES "RC1"("RC1TDOC", "RC1NDOC") ON DELETE CASCADE
)
CREATE INDEX "RC1a01" ON "RC1a" (
	"RC1TDOC",
	"RC1NDOC"
)


--  ==============================================================================================