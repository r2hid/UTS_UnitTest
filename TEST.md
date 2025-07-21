graph TD
    subgraph Sumber Data OLTP
        A[Sistem POS] --> B(Ekstrak Data Penjualan)
        C[Sistem ERP] --> D(Ekstrak Data Produk & Inventaris)
        E[Sistem CRM] --> F(Ekstrak Data Pelanggan)
        G[Sistem E-commerce] --> H(Ekstrak Data Penjualan Online & Perilaku)
        I[Spreadsheet/File Lainnya] --> J(Ekstrak Data Promosi)
    end

    subgraph Area Pementasan (Staging Area)
        B --> K{Data Mentah Penjualan}
        D --> L{Data Mentah Produk & Inventaris}
        F --> M{Data Mentah Pelanggan}
        H --> N{Data Mentah Penjualan Online & Perilaku}
        J --> O{Data Mentah Promosi}
    end

    subgraph Fase Transformasi
        K --> P(Pembersihan & Standardisasi Penjualan)
        L --> Q(Pembersihan & Standardisasi Produk/Inventaris)
        M --> R(Pembersihan & Standardisasi Pelanggan)
        N --> S(Pembersihan & Standardisasi Penjualan Online)
        O --> T(Pembersihan & Standardisasi Promosi)

        P --> U(Integrasi Data Penjualan & Agregasi)
        Q --> V(Manajemen Dimensi Produk & Inventaris)
        R --> W(Manajemen Dimensi Pelanggan - SCD)
        S --> U
        T --> U

        U --> X(Penetapan Kunci Surrogate)
        V --> X
        W --> X
    end

    subgraph Data Warehouse
        X --> Y[Tabel Fakta Penjualan]
        X --> Z[Dimensi Waktu]
        X --> AA[Dimensi Produk]
        X --> BB[Dimensi Pelanggan]
        X --> CC[Dimensi Toko/Lokasi]
        X --> DD[Dimensi Promosi]
    end

    subgraph Pengguna & Alat BI
        Y --> EE[Laporan & Dasbor]
        Z --> EE
        AA --> EE
        BB --> EE
        CC --> EE
        DD --> EE
    end

    style A fill:#a2e0a2,stroke:#333,stroke-width:2px
    style C fill:#a2e0a2,stroke:#333,stroke-width:2px
    style E fill:#a2e0a2,stroke:#333,stroke-width:2px
    style G fill:#a2e0a2,stroke:#333,stroke-width:2px
    style I fill:#a2e0a2,stroke:#333,stroke-width:2px

    style B fill:#f9f9f9,stroke:#333,stroke-width:1px
    style D fill:#f9f9f9,stroke:#333,stroke-width:1px
    style F fill:#f9f9f9,stroke:#333,stroke-width:1px
    style H fill:#f9f9f9,stroke:#333,stroke-width:1px
    style J fill:#f9f9f9,stroke:#333,stroke-width:1px

    style K fill:#fffacd,stroke:#333,stroke-width:1px
    style L fill:#fffacd,stroke:#333,stroke-width:1px
    style M fill:#fffacd,stroke:#333,stroke-width:1px
    style N fill:#fffacd,stroke:#333,stroke-width:1px
    style O fill:#fffacd,stroke:#333,stroke-width:1px

    style P fill:#add8e6,stroke:#333,stroke-width:2px
    style Q fill:#add8e6,stroke:#333,stroke-width:2px
    style R fill:#add8e6,stroke:#333,stroke-width:2px
    style S fill:#add8e6,stroke:#336,stroke-width:2px
    style T fill:#add8e6,stroke:#333,stroke-width:2px
    style U fill:#add8e6,stroke:#333,stroke-width:2px
    style V fill:#add8e6,stroke:#333,stroke-width:2px
    style W fill:#add8e6,stroke:#333,stroke-width:2px
    style X fill:#add8e6,stroke:#333,stroke-width:2px

    style Y fill:#90ee90,stroke:#333,stroke-width:2px
    style Z fill:#90ee90,stroke:#333,stroke-width:2px
    style AA fill:#90ee90,stroke:#333,stroke-width:2px
    style BB fill:#90ee90,stroke:#333,stroke-width:2px
    style CC fill:#90ee90,stroke:#333,stroke-width:2px
    style DD fill:#90ee90,stroke:#333,stroke-width:2px

    style EE fill:#dda0dd,stroke:#333,stroke-width:2px
