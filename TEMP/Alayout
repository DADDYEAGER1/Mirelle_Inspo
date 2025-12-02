import type { Metadata } from "next";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Script from "next/script";
import NewsletterPopup from "@/components/NewsletterPopup"; // ✅ NEW: Phase 3 Newsletter Popup
import { Inter, Cormorant_Garamond } from 'next/font/google';
import { generatePersonSchema } from '@/lib/generateSchemas';

const inter = Inter({
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-inter',
});

const cormorant = Cormorant_Garamond({
  weight: ['400', '600', '700'],
  subsets: ['latin'],
  display: 'swap',
  variable: '--font-cormorant',
});

export const metadata: Metadata = {
  metadataBase: new URL('https://mirelleinspo.com'),
  title: {
    default: "Mirellè Inspo | 1K+ Nail Designs Everyone's Saving for 2025-2026",
    template: "%s | Mirellè Inspo"
  },
  description: "Get 1,000+ trending nail designs used by 50K+ nail lovers. Chrome, cat claw, milky pastels dominating 2026. DIY tutorials, seasonal collections, press-ons from $3.99. Save yours!",
  keywords: [
    "nail designs 2025",
    "nail trends 2026",
    "chrome nails 2025",
    "cat claw nails",
    "milky nail trends",
    "square nails 2026",
    "3D nail art",
    "press-on nails cheap",
    "DIY nail tutorials",
    "seasonal nail designs",
    "popsicle nail colors",
    "pearl finish nails",
    "trending nail ideas",
    "Pinterest nail inspiration",
    "TikTok viral nails"
  ],
  authors: [{ name: "Mirellè Inspo Team", url: "https://mirelleinspo.com/about" }],
  creator: "Mirellè Inspo",
  publisher: "Mirellè Inspo",
  formatDetection: {
    telephone: false,
    email: false,
    address: false,
  },
  
  other: {
    'distribution': 'global',
    'rating': 'general',
    'coverage': 'worldwide',
    'target': 'all',
    'audience': 'all',
    'language': 'en-US',
    'classification': 'Beauty, Fashion, Nail Art, DIY Tutorials, Press-On Nails, Lifestyle',
    'referrer': 'always',
    'revisit-after': '7 days',
    
    'pinterest-rich-pin': 'true',
    'pinterest:partner': 'true',
    
    'og:site_name': 'Mirellè Inspo',
    'og:locale': 'en_US',
    'og:locale:alternate': 'en_GB',
  },
  
  openGraph: {
    type: "website",
    locale: "en_US",
    url: "https://mirelleinspo.com",
    siteName: "Mirellè Inspo",
    title: "Mirellè Inspo | 1K+ Nail Designs Everyone's Saving for 2025-2026",
    description: "Join 50K+ getting chrome, cat claw & milky pastel nails dominating 2026. Press-ons from $3.99, DIY tutorials, trending designs. Your next obsession awaits!",
    images: [
      {
        url: "/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Mirellè Inspo - 1000+ trending nail designs for 2025-2026 including chrome, cat claw and square nails",
      },
    ],
  },
  
  twitter: {
    card: "summary_large_image",
    title: "Mirellè Inspo | 1K+ Designs 50K+ Are Saving Right Now",
    description: "Chrome, cat claw, milky pastels taking over 2026. Press-ons $3.99+, DIY tutorials, trending collections. Join 50K+ nail obsessed!",
    images: ["/twitter-image.jpg"],
    creator: "@mirelleinspo",
    site: "@mirelleinspo",
  },
  
  robots: {
    index: true,
    follow: true,
    nocache: false,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  
  icons: {
    icon: [
      { url: "/favicon.ico", sizes: "48x48" },
      { url: "/favicon.svg", type: "image/svg+xml" },
      { url: "/favicon-16x16.png", sizes: "16x16", type: "image/png" },
      { url: "/favicon-32x32.png", sizes: "32x32", type: "image/png" },
    ],
    apple: [
      { url: "/apple-touch-icon.png", sizes: "180x180", type: "image/png" },
    ],
  },
  
  manifest: "/site.webmanifest",
  
  alternates: {
    canonical: "https://mirelleinspo.com",
    languages: {
      'en-US': 'https://mirelleinspo.com',
      'en-GB': 'https://mirelleinspo.com',
      'en-CA': 'https://mirelleinspo.com',
      'en-AU': 'https://mirelleinspo.com',
      'en': 'https://mirelleinspo.com',
    },
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const baseUrl = 'https://mirelleinspo.com';
  
  // Enhanced structured data for AI bots
const organizationSchema = {
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": `${baseUrl}/#organization`,
  "name": "Mirellé",
  "alternateName": "Mirelle",
  "url": baseUrl,
  "logo": {
    "@type": "ImageObject",
    "url": `${baseUrl}/apple-touch-icon.png`,
    "width": 512,
    "height": 512
  },
  "description": "Expert nail art inspiration, tutorials, and seasonal beauty trends for modern women",
  "sameAs": [
    "https://www.pinterest.com/mirelle_inspo",
    "https://www.instagram.com/mirelle_inspo",
    "https://www.wikidata.org/wiki/mirelle_inspo",
    "https://x.com/mirelleinspo",
    "https://www.wikidata.org/wiki/Q136769265",
  ],
  
  // 🆕 ADD PINTEREST-SPECIFIC SCHEMA
  "image": `${baseUrl}/og-image.jpg`,
  "potentialAction": {
    "@type": "InteractAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://www.pinterest.com/pin/create/button/?url={url}&media={media}&description={description}",
      "actionPlatform": [
        "http://schema.org/DesktopWebPlatform",
        "http://schema.org/MobileWebPlatform"
      ]
    },
    "name": "Save to Pinterest"
  },

    "contactPoint": {
      "@type": "ContactPoint",
      "contactType": "Customer Service",
      "url": `${baseUrl}/contact`
    },

    "areaServed": {
      "@type": "Place",
      "name": "Worldwide"
    },
    "audience": {
      "@type": "Audience",
      "audienceType": "Global",
      "geographicArea": {
        "@type": "Place",
        "name": "Worldwide"
      }
    }
  };

  const websiteSchema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": `${baseUrl}/#website`,
    "name": "Mirellé",
    "url": baseUrl,
    "description": "Nail art ideas, trends, tutorials, and inspiration for 2025. Professional tips for beautiful, healthy nails.",
    "publisher": {
      "@type": "Organization",
      "@id": `${baseUrl}/#organization`,
      "name": "Mirellé",
    },
    "inLanguage": "en-US",
    "potentialAction": {
      "@type": "SearchAction",
      "target": {
        "@type": "EntryPoint",
        "urlTemplate": `${baseUrl}/search?q={search_term_string}`
      },
      "query-input": "required name=search_term_string"
    }
  };

  // NEW: Generate Person schema for author entity
  const personSchema = generatePersonSchema();

  // BreadcrumbList for better content structure
  const breadcrumbSchema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": baseUrl
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Blog",
        "item": `${baseUrl}/blog`
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Topics",
        "item": `${baseUrl}/topics`
      }
    ]
  };

  return (
    <html lang="en-US">
      <head>
        {/* Global geo-targeting meta tags (won't hurt international reach) */}
        <meta name="distribution" content="global" />
        <meta name="coverage" content="worldwide" />
        <meta name="target" content="all" />
        <meta name="audience" content="all" />
        <meta httpEquiv="content-language" content="en-US" />
        <meta name="language" content="English" />
        <meta name="rating" content="general" />
        <meta name="revisit-after" content="7 days" />
        
        {/* AI Bot friendly meta tags */}
        <meta name="referrer" content="always" />
        <meta name="classification" content="Beauty, Fashion, Nail Art, Tutorials, DIY, Lifestyle" />
        

        {/* ✅ KEEP THESE */}
        <link rel="preconnect" href="https://pagead2.googlesyndication.com" />
        <link rel="dns-prefetch" href="https://www.googletagmanager.com" />
        
        {/* Fonts with display=swap for better performance */}
        <link
          href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap"
          rel="stylesheet"
        />

        {/* AdSense verification meta tag */}
        <meta name="google-adsense-account" content="ca-pub-1145734682794444" />
        
        {/* Pinterest Save Button Script */}
        {/* <script async defer src="//assets.pinterest.com/js/pinit.js"></script> */}
      </head>

      <body 
        className={`${inter.variable} ${cormorant.variable} antialiased`}
        suppressHydrationWarning
      >
        {/* Google Tag Manager (noscript) */}
        <noscript>
          <iframe
            src="https://www.googletagmanager.com/ns.html?id=GTM-WPW9XBW8"
            height="0"
            width="0"
            style={{ display: "none", visibility: "hidden" }}
            title="Google Tag Manager"
          ></iframe>
        </noscript>

        {/* GA4 Analytics */}
        <Script
          src="https://www.googletagmanager.com/gtag/js?id=G-4BZ9QKQZ73"
          strategy="afterInteractive"
        />
        <Script id="ga4-init" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'G-4BZ9QKQZ73', {
              page_path: window.location.pathname,
              send_page_view: true
            });
          `}
        </Script>

{/* Google AdSense */}
        
        {/* Preload critical font */}
        <link
          rel="preload"
          href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap"
          as="style"
        />


        {/* Mobile web app meta */}
        <meta name="mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-capable" content="yes" />
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />
        <meta name="format-detection" content="telephone=no" />
        <meta name="format-detection" content="email=no" />
        <meta name="format-detection" content="address=no" />
        <meta name="apple-mobile-web-app-title" content="Mirellé" />
        <meta name="application-name" content="Mirellé" />

        {/* Theme color */}
        <meta name="theme-color" content="#8b1f42" />
        
        {/* ADD WEB VITALS TRACKING HERE - AFTER ADSENSE */}
        <Script id="web-vitals" strategy="afterInteractive">
          {`
            (function() {
              function sendToAnalytics(metric) {
                if (window.gtag) {
                  window.gtag('event', metric.name, {
                    value: Math.round(metric.name === 'CLS' ? metric.value * 1000 : metric.value),
                    event_category: 'Web Vitals',
                    event_label: metric.id,
                    non_interaction: true,
                  });
                }
              }
              
              if ('PerformanceObserver' in window) {
                // Track Largest Contentful Paint (LCP)
                try {
                  const lcpObserver = new PerformanceObserver((list) => {
                    const entries = list.getEntries();
                    const lastEntry = entries[entries.length - 1];
                    sendToAnalytics({
                      name: 'LCP',
                      value: lastEntry.renderTime || lastEntry.loadTime,
                      id: 'v1-' + Date.now()
                    });
                  });
                  lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
                } catch (e) {}
                
                // Track First Input Delay (FID)
                try {
                  const fidObserver = new PerformanceObserver((list) => {
                    const entries = list.getEntries();
                    entries.forEach((entry) => {
                      sendToAnalytics({
                        name: 'FID',
                        value: entry.processingStart - entry.startTime,
                        id: 'v1-' + Date.now()
                      });
                    });
                  });
                  fidObserver.observe({ entryTypes: ['first-input'] });
                } catch (e) {}
                
                // Track Cumulative Layout Shift (CLS)
                try {
                  let clsValue = 0;
                  const clsObserver = new PerformanceObserver((list) => {
                    list.getEntries().forEach((entry) => {
                      if (!entry.hadRecentInput) {
                        clsValue += entry.value;
                      }
                    });
                  });
                  clsObserver.observe({ entryTypes: ['layout-shift'] });
                  
                  // Send CLS on page hide
                  addEventListener('visibilitychange', () => {
                    if (document.visibilityState === 'hidden') {
                      sendToAnalytics({
                        name: 'CLS',
                        value: clsValue,
                        id: 'v1-' + Date.now()
                      });
                    }
                  });
                } catch (e) {}
              }
            })();
          `}
        </Script>

        {/* Enhanced Structured Data for AI Understanding */}
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(organizationSchema),
          }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(websiteSchema),
          }}
        />
        {/* NEW: Person Schema for Author Entity */}
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(personSchema),
          }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(breadcrumbSchema),
          }}
        />

        <Header />
        <main className="min-h-screen" id="main-content" role="main">
          {children}
        </main>
        <Footer />
        <NewsletterPopup /> {/* ✅ NEW: Phase 3 - Newsletter popup with timing triggers */}
      </body>
    </html>
  );
}
