import Link from 'next/link';
import { Metadata } from 'next';

// SEO Metadata
export const metadata: Metadata = {
  title: 'Nail Care Topics & Expert Guides | Long Reads on Nail Trends 2026',
  description: 'In-depth editorial guides on nail care, trending techniques, seasonal styles, and professional tips. Expert journalism for nail enthusiasts.',
  keywords: 'nail care guides, chrome nails tutorial, nail art techniques, seasonal nail trends, professional manicure tips, nail health editorial, beauty journalism',
  authors: [{ name: 'Mirellè Editorial Team' }],
  creator: 'Mirellè Inspo',
  publisher: 'Mirellè Inspo',
  alternates: {
    canonical: 'https://mirelleinspo.com/topics',
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  openGraph: {
    title: 'Nail Care Topics & Expert Guides | Mirellè Inspo',
    description: 'In-depth editorial guides on nail care, trending techniques, and professional tips.',
    type: 'website',
    url: 'https://mirelleinspo.com/topics',
    siteName: 'Mirellè Inspo',
    locale: 'en_US',
    images: [{
      url: 'https://mirelleinspo.com/og-topics.jpg',
      width: 1200,
      height: 630,
      alt: 'Mirellè Inspo Topics and Editorial Guides',
    }],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Nail Care Topics & Expert Guides | Mirellè Inspo',
    description: 'In-depth editorial guides on nail care and trending techniques.',
    images: ['https://mirelleinspo.com/twitter-topics.jpg'],
    creator: '@mirelleinspo',
  },
}

const topics = [
  {
    title: "Nail Care Guide",
    description: "Essential tips for healthy, beautiful nails - from basic care to advanced treatments",
    image: "/nailcare.jpg",
    href: "/topics/nail-care-guide",
    category: "HEALTH"
  },
  {
    title: "For Skin Tones",
    description: "Find the perfect nail colors for your skin tone with expert color matching",
    image: "/skintone.jpg",
    href: "/topics/skin-tones",
    category: "COLOR THEORY"
  },
  {
    title: "Nail Art Guides",
    description: "Step-by-step tutorials from beginner techniques to advanced designs",
    image: "/nailart.jpg",
    href: "/topics/nail-art-guides",
    category: "TECHNIQUE"
  },
  {
    title: "Seasonal Trends",
    description: "Latest seasonal nail trends - spring florals, summer brights, fall warmth, winter elegance",
    image: "/nailtrends.jpg",
    href: "/topics/seasonal-trends",
    category: "TRENDS"
  },
  {
    title: "At-Home Nail Hacks",
    description: "Professional techniques you can do at home - DIY manicures and salon-quality results",
    image: "/athome.jpg",
    href: "/topics/at-home-hacks",
    category: "DIY"
  },
  {
    title: "Modern Women Inspiration",
    description: "Empowering nail looks for the modern woman - chic, confident styles for work and life",
    image: "/modern.jpg",
    href: "/topics/modern-women",
    category: "LIFESTYLE"
  }
];

export default function Topics() {
  // JSON-LD Structured Data
  const websiteSchema = {
    '@context': 'https://schema.org',
    '@type': 'CollectionPage',
    '@id': 'https://mirelleinspo.com/topics',
    name: 'Nail Care Topics & Expert Guides',
    description: 'Comprehensive editorial guides covering nail care, art, trends, and professional techniques',
    url: 'https://mirelleinspo.com/topics',
    inLanguage: 'en-US',
  };

  const breadcrumbSchema = {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: [
      {
        '@type': 'ListItem',
        position: 1,
        name: 'Home',
        item: 'https://mirelleinspo.com',
      },
      {
        '@type': 'ListItem',
        position: 2,
        name: 'Topics',
        item: 'https://mirelleinspo.com/topics',
      },
    ],
  };

  return (
    <>
      {/* Structured Data */}
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(websiteSchema) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(breadcrumbSchema) }} />

      <main className="min-h-screen bg-background">
        {/* Editorial Hero - Featured Long Read */}
        <section className="border-b border-foreground/10">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-20">
            <div className="mb-8 md:mb-12">
              <span className="font-ui text-xs tracking-wider text-foreground/60 uppercase">
                Long Reads
              </span>
            </div>

            <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12">
              {/* Featured Image */}
              <div className="lg:col-span-7">
                <Link href={topics[0].href} className="group block">
                  <div className="relative w-full overflow-hidden bg-foreground/5">
                    <div className="relative w-full pb-[66%]">
                      <img
                        src={topics[0].image}
                        alt={topics[0].title}
                        className="absolute inset-0 w-full h-full object-cover transition-opacity duration-500 group-hover:opacity-90"
                      />
                    </div>
                  </div>
                </Link>
              </div>

              {/* Featured Content */}
              <div className="lg:col-span-5 flex flex-col justify-center">
                <Link href={topics[0].href} className="group">
                  <span className="font-ui text-xs tracking-wider text-foreground/60 uppercase mb-4 block">
                    {topics[0].category}
                  </span>
                  
                  <h1 className="font-heading text-3xl sm:text-4xl md:text-5xl lg:text-6xl text-foreground mb-6 leading-tight group-hover:text-foreground/70 transition-colors duration-300">
                    {topics[0].title}
                  </h1>
                  
                  <p className="font-body text-base md:text-lg text-foreground/70 leading-relaxed mb-8">
                    {topics[0].description}
                  </p>

                  <span className="font-ui text-sm text-foreground border-b border-foreground inline-block pb-1 group-hover:border-foreground/50 transition-colors duration-300">
                    Read More
                  </span>
                </Link>
              </div>
            </div>
          </div>
        </section>

        {/* All Topics Grid - Editorial Style */}
        <section className="py-12 md:py-20">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="mb-12 md:mb-16">
              <h2 className="font-heading text-2xl md:text-4xl text-foreground mb-4">
                Explore Topics
              </h2>
              <p className="font-body text-base md:text-lg text-foreground/70 max-w-2xl">
                Comprehensive guides covering every aspect of nail care, from fundamentals to advanced techniques.
              </p>
            </div>

            {/* Grid - Masonry style on larger screens */}
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-x-6 gap-y-12 md:gap-x-8 md:gap-y-16">
              {topics.slice(1).map((topic, index) => (
                <article key={index} className="group">
                  <Link href={topic.href} className="block">
                    {/* Image */}
                    <div className="relative w-full overflow-hidden bg-foreground/5 mb-5">
                      <div className="relative w-full pb-[75%]">
                        <img
                          src={topic.image}
                          alt={topic.title}
                          className="absolute inset-0 w-full h-full object-cover transition-opacity duration-500 group-hover:opacity-90"
                        />
                      </div>
                    </div>

                    {/* Content */}
                    <div className="space-y-3">
                      <span className="font-ui text-xs tracking-wider text-foreground/60 uppercase block">
                        {topic.category}
                      </span>
                      
                      <h3 className="font-heading text-xl md:text-2xl text-foreground leading-tight group-hover:text-foreground/70 transition-colors duration-300">
                        {topic.title}
                      </h3>
                      
                      <p className="font-body text-sm md:text-base text-foreground/70 leading-relaxed">
                        {topic.description}
                      </p>
                    </div>
                  </Link>
                </article>
              ))}
            </div>
          </div>
        </section>

        {/* Related Sections - Minimal Editorial */}
        <section className="border-t border-foreground/10 py-12 md:py-20">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 className="font-heading text-2xl md:text-3xl text-foreground mb-8 md:mb-12">
              More from Mirellè
            </h2>

            <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 md:gap-8">
              {/* Blog */}
              <Link
                href="/blog"
                className="group border border-foreground/10 p-8 md:p-10 hover:border-foreground/30 transition-all duration-300"
              >
                <span className="font-ui text-xs tracking-wider text-foreground/60 uppercase block mb-4">
                  Editorial
                </span>
                <h3 className="font-heading text-xl md:text-2xl text-foreground mb-3 group-hover:text-foreground/70 transition-colors">
                  Nail Trends
                </h3>
                <p className="font-body text-sm text-foreground/70">
                  Latest insights and analysis
                </p>
              </Link>

              {/* Inspo */}
              <Link
                href="/inspo"
                className="group border border-foreground/10 p-8 md:p-10 hover:border-foreground/30 transition-all duration-300"
              >
                <span className="font-ui text-xs tracking-wider text-foreground/60 uppercase block mb-4">
                  Gallery
                </span>
                <h3 className="font-heading text-xl md:text-2xl text-foreground mb-3 group-hover:text-foreground/70 transition-colors">
                  Inspiration
                </h3>
                <p className="font-body text-sm text-foreground/70">
                  Curated visual stories
                </p>
              </Link>

              {/* Shop */}
              <Link
                href="/shop"
                className="group border border-foreground/10 p-8 md:p-10 hover:border-foreground/30 transition-all duration-300"
              >
                <span className="font-ui text-xs tracking-wider text-foreground/60 uppercase block mb-4">
                  Collection
                </span>
                <h3 className="font-heading text-xl md:text-2xl text-foreground mb-3 group-hover:text-foreground/70 transition-colors">
                  Press-On Nails
                </h3>
                <p className="font-body text-sm text-foreground/70">
                  Thoughtfully designed sets
                </p>
              </Link>
            </div>
          </div>
        </section>
      </main>
    </>
  );
}
