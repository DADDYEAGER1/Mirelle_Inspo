import { Metadata } from 'next';
import Link from 'next/link';
import Image from 'next/image';

export const metadata: Metadata = {
  title: "Mirellé - Premium Nail Art Inspiration, Trends & Expert Tutorials",
  description: "Your editorial platform for nail art inspiration, expert tutorials, curated product reviews, and the latest nail trends. Join 50K+ nail enthusiasts worldwide for premium nail content and at-home manicure guides.",
  keywords: "nail art inspiration, nail trends 2026, nail art blog, DIY nail designs at home, nail care tips, nail art tutorials, curated nail products, nail enthusiasts community, editorial nail content, expert nail advice, at-home manicure guides, nail design inspiration, premium nail blog",
  alternates: {
    canonical: 'https://mirelleinspo.com',
  },
  openGraph: {
    title: "Mirellé - Premium Nail Art Inspiration & Editorial Content Platform",
    description: "Join 50K+ nail enthusiasts. Get expert tutorials, trend forecasts, curated products, and editorial nail content. 1M weekly Pinterest views.",
    url: 'https://mirelleinspo.com',
    siteName: 'Mirellé Inspo',
    type: 'website',
  },
};

const jsonLd = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Mirellé Inspo",
  "description": "Premium editorial platform for nail art inspiration, expert tutorials, trends, and curated product recommendations",
  "url": "https://mirelleinspo.com",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://mirelleinspo.com/search?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
};

export default function HomePage() {
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
      />
      
      <div className="min-h-screen bg-background">
        {/* Hero Section */}
        <section className="py-24 bg-background">
          <div className="max-w-6xl mx-auto px-6 sm:px-8 lg:px-12">
            <div className="text-center max-w-4xl mx-auto">
              <h1 className="font-heading text-5xl md:text-6xl lg:text-7xl text-foreground mb-8 leading-tight">
                Your Premier Nail Art Inspiration & Editorial Content Platform
              </h1>
              <p className="font-body text-xl md:text-2xl text-foreground leading-relaxed mb-12">
                Discover expert nail tutorials, curated trend forecasts, and premium editorial content for nail enthusiasts worldwide. From at-home manicures to professional techniques, elevate your nail artistry with Mirellé.
              </p>
              <div className="flex flex-wrap justify-center gap-4 font-ui text-sm text-foreground">
                <span>50K Monthly Readers</span>
                <span className="text-foreground/20">•</span>
                <span>1M Weekly Pinterest Views</span>
                <span className="text-foreground/20">•</span>
                <span>Global Nail Community</span>
              </div>
            </div>
          </div>
        </section>

        {/* About Mirellé Section */}
        <section className="py-20 bg-background border-y border-foreground/10">
          <div className="max-w-6xl mx-auto px-6 sm:px-8 lg:px-12">
            <div className="text-center mb-16">
              <h2 className="font-heading text-4xl md:text-5xl text-foreground mb-6">
                About Mirellé
              </h2>
              <p className="font-body text-lg text-foreground leading-relaxed max-w-3xl mx-auto">
                Mirellé is a premium editorial platform dedicated exclusively to nail art inspiration, education, and community. We serve nail enthusiasts across the globe with expertly curated content, in-depth tutorials, trend analyses, and product recommendations designed for at-home nail care and professional-level techniques.
              </p>
            </div>

            <div className="grid md:grid-cols-3 gap-12">
              <div className="text-center">
                <div className="mb-6">
                  <div className="w-20 h-20 border-2 border-foreground mx-auto flex items-center justify-center">
                    <svg className="w-10 h-10 text-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24" strokeWidth={1.5}>
                      <path strokeLinecap="round" strokeLinejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25" />
                    </svg>
                  </div>
                </div>
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  Editorial Excellence
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed">
                  Every piece of content undergoes rigorous editorial review to ensure accuracy, quality, and value for our community of nail enthusiasts.
                </p>
              </div>

              <div className="text-center">
                <div className="mb-6">
                  <div className="w-20 h-20 border-2 border-foreground mx-auto flex items-center justify-center">
                    <svg className="w-10 h-10 text-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24" strokeWidth={1.5}>
                      <path strokeLinecap="round" strokeLinejoin="round" d="M4.26 10.147a60.436 60.436 0 00-.491 6.347A48.627 48.627 0 0112 20.904a48.627 48.627 0 018.232-4.41 60.46 60.46 0 00-.491-6.347m-15.482 0a50.57 50.57 0 00-2.658-.813A59.905 59.905 0 0112 3.493a59.902 59.902 0 0110.399 5.84c-.896.248-1.783.52-2.658.814m-15.482 0A50.697 50.697 0 0112 13.489a50.702 50.702 0 017.74-3.342M6.75 15a.75.75 0 100-1.5.75.75 0 000 1.5zm0 0v-3.675A55.378 55.378 0 0112 8.443m-7.007 11.55A5.981 5.981 0 006.75 15.75v-1.5" />
                    </svg>
                  </div>
                </div>
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  Expert-Driven Content
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed">
                  Our team collaborates with experienced nail artists and salon professionals to deliver authentic, technique-focused tutorials and trend insights.
                </p>
              </div>

              <div className="text-center">
                <div className="mb-6">
                  <div className="w-20 h-20 border-2 border-foreground mx-auto flex items-center justify-center">
                    <svg className="w-10 h-10 text-foreground" fill="none" stroke="currentColor" viewBox="0 0 24 24" strokeWidth={1.5}>
                      <path strokeLinecap="round" strokeLinejoin="round" d="M18 18.72a9.094 9.094 0 003.741-.479 3 3 0 00-4.682-2.72m.94 3.198l.001.031c0 .225-.012.447-.037.666A11.944 11.944 0 0112 21c-2.17 0-4.207-.576-5.963-1.584A6.062 6.062 0 016 18.719m12 0a5.971 5.971 0 00-.941-3.197m0 0A5.995 5.995 0 0012 12.75a5.995 5.995 0 00-5.058 2.772m0 0a3 3 0 00-4.681 2.72 8.986 8.986 0 003.74.477m.94-3.197a5.971 5.971 0 00-.94 3.197M15 6.75a3 3 0 11-6 0 3 3 0 016 0zm6 3a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0zm-13.5 0a2.25 2.25 0 11-4.5 0 2.25 2.25 0 014.5 0z" />
                    </svg>
                  </div>
                </div>
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  Community Focused
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed">
                  We answer reader questions, feature community creations, and foster a supportive space for nail enthusiasts at every skill level.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* What We Offer Section */}
        <section className="py-20 bg-background">
          <div className="max-w-6xl mx-auto px-6 sm:px-8 lg:px-12">
            <div className="text-center mb-16">
              <h2 className="font-heading text-4xl md:text-5xl text-foreground mb-6">
                What We Offer
              </h2>
              <p className="font-body text-lg text-foreground leading-relaxed max-w-3xl mx-auto">
                Comprehensive nail content for enthusiasts seeking inspiration, education, and expert guidance for at-home and professional nail artistry.
              </p>
            </div>

            <div className="grid md:grid-cols-2 gap-8">
              <div className="bg-background border border-foreground/10 p-8">
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  Nail Art Trends & Forecasts
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed mb-6">
                  Stay ahead of the curve with our expertly curated trend reports, seasonal forecasts, and analysis of emerging nail art styles from around the world. From runway-inspired designs to street style trends, we decode what's next in nail fashion.
                </p>
                <Link 
                  href="/trends" 
                  className="font-ui text-sm text-foreground uppercase tracking-wide underline hover:opacity-70 transition-opacity"
                >
                  Explore Trends
                </Link>
              </div>

              <div className="bg-background border border-foreground/10 p-8">
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  Expert Tutorials & Techniques
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed mb-6">
                  Master professional techniques with our detailed step-by-step tutorials. Whether you're perfecting basic manicure skills or attempting advanced nail art, our guides break down complex techniques into achievable steps for at-home execution.
                </p>
                <Link 
                  href="/tutorials" 
                  className="font-ui text-sm text-foreground uppercase tracking-wide underline hover:opacity-70 transition-opacity"
                >
                  View Tutorials
                </Link>
              </div>

              <div className="bg-background border border-foreground/10 p-8">
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  Curated Product Recommendations
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed mb-6">
                  Discover our editorial team's handpicked selection of nail products, tools, and accessories. Every recommendation is thoroughly tested and evaluated to ensure quality, performance, and value for at-home nail enthusiasts and professionals alike.
                </p>
                <Link 
                  href="/products" 
                  className="font-ui text-sm text-foreground uppercase tracking-wide underline hover:opacity-70 transition-opacity"
                >
                  Browse Products
                </Link>
              </div>

              <div className="bg-background border border-foreground/10 p-8">
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  In-Depth Editorial Content
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed mb-6">
                  Dive into long-form articles exploring nail care science, historical perspectives on nail fashion, interviews with industry professionals, and comprehensive guides covering every aspect of nail health, artistry, and culture.
                </p>
                <Link 
                  href="/blog" 
                  className="font-ui text-sm text-foreground uppercase tracking-wide underline hover:opacity-70 transition-opacity"
                >
                  Read Articles
                </Link>
              </div>
            </div>
          </div>
        </section>

        {/* Our Approach Section */}
        <section className="py-20 bg-background border-y border-foreground/10">
          <div className="max-w-4xl mx-auto px-6 sm:px-8 lg:px-12">
            <div className="text-center mb-12">
              <h2 className="font-heading text-4xl md:text-5xl text-foreground mb-6">
                Our Approach
              </h2>
            </div>

            <div className="space-y-12">
              <div>
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  At-Home Nail Enthusiasts First
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed">
                  While we appreciate professional nail artistry, our primary focus is empowering individuals who love creating beautiful nails at home. We design our tutorials, product recommendations, and trend guides with the at-home manicure experience in mind, ensuring techniques are accessible and achievable without professional equipment or training.
                </p>
              </div>

              <div>
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  Collaboration for Relevance
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed">
                  We collaborate with salon professionals and independent nail artists to ensure our content remains current, technically accurate, and reflective of real-world nail artistry. These partnerships enhance the quality and relevance of information we provide to our community without compromising our editorial independence.
                </p>
              </div>

              <div>
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  Community Questions Answered
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed">
                  Our expert team actively responds to reader questions, addressing common challenges, troubleshooting technique issues, and providing personalized guidance. Your questions shape our content calendar, ensuring we create resources that address real needs within the nail enthusiast community.
                </p>
              </div>

              <div>
                <h3 className="font-heading text-2xl text-foreground mb-4">
                  Editorial Integrity
                </h3>
                <p className="font-body text-base text-foreground leading-relaxed">
                  Mirellé operates with complete editorial independence. Our product recommendations are based solely on quality, performance, and value. We curate products we genuinely believe benefit our readers, maintaining transparency about our selection process and any affiliate relationships.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Global Community Section */}
        <section className="py-20 bg-background">
          <div className="max-w-6xl mx-auto px-6 sm:px-8 lg:px-12">
            <div className="text-center mb-12">
              <h2 className="font-heading text-4xl md:text-5xl text-foreground mb-6">
                A Global Nail Enthusiast Community
              </h2>
              <p className="font-body text-lg text-foreground leading-relaxed max-w-3xl mx-auto">
                Mirellé serves nail lovers worldwide, creating a space where passion for nail artistry transcends borders, skill levels, and backgrounds. Our community spans continents, united by appreciation for beautiful, creative, and expertly executed nail designs.
              </p>
            </div>

            <div className="grid md:grid-cols-3 gap-8 text-center">
              <div>
                <div className="font-heading text-5xl text-foreground mb-2">50K+</div>
                <p className="font-body text-base text-foreground">Monthly readers seeking nail inspiration and expertise</p>
              </div>
              <div>
                <div className="font-heading text-5xl text-foreground mb-2">1M+</div>
                <p className="font-body text-base text-foreground">Weekly Pinterest views of our curated nail content</p>
              </div>
              <div>
                <div className="font-heading text-5xl text-foreground mb-2">Global</div>
                <p className="font-body text-base text-foreground">Nail enthusiasts from every corner of the world</p>
              </div>
            </div>
          </div>
        </section>

        {/* Content Categories Section */}
        <section className="py-20 bg-background border-y border-foreground/10">
          <div className="max-w-6xl mx-auto px-6 sm:px-8 lg:px-12">
            <div className="text-center mb-16">
              <h2 className="font-heading text-4xl md:text-5xl text-foreground mb-6">
                Explore Our Content
              </h2>
            </div>

            <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
              <Link 
                href="/topics/seasonal-trends"
                className="group border border-foreground/10 p-8 hover:border-foreground/30 transition-all"
              >
                <h3 className="font-heading text-xl text-foreground mb-3">Trends</h3>
                <p className="font-body text-sm text-foreground leading-relaxed mb-4">
                  Seasonal forecasts, emerging styles, and runway-inspired nail art
                </p>
                <span className="font-ui text-xs text-foreground uppercase tracking-wide group-hover:underline">
                  View Trends →
                </span>
              </Link>

              <Link 
                href="/topics/nail-art-guides"
                className="group border border-foreground/10 p-8 hover:border-foreground/30 transition-all"
              >
                <h3 className="font-heading text-xl text-foreground mb-3">Tutorials</h3>
                <p className="font-body text-sm text-foreground leading-relaxed mb-4">
                  Step-by-step guides for mastering techniques at home
                </p>
                <span className="font-ui text-xs text-foreground uppercase tracking-wide group-hover:underline">
                  Learn Techniques →
                </span>
              </Link>

              <Link 
                href="/shop"
                className="group border border-foreground/10 p-8 hover:border-foreground/30 transition-all"
              >
                <h3 className="font-heading text-xl text-foreground mb-3">Products</h3>
                <p className="font-body text-sm text-foreground leading-relaxed mb-4">
                  Curated recommendations tested by our editorial team
                </p>
                <span className="font-ui text-xs text-foreground uppercase tracking-wide group-hover:underline">
                  Browse Products →
                </span>
              </Link>

              <Link 
                href="/blog"
                className="group border border-foreground/10 p-8 hover:border-foreground/30 transition-all"
              >
                <h3 className="font-heading text-xl text-foreground mb-3">Blog</h3>
                <p className="font-body text-sm text-foreground leading-relaxed mb-4">
                  In-depth articles, interviews, and nail culture insights
                </p>
                <span className="font-ui text-xs text-foreground uppercase tracking-wide group-hover:underline">
                  Read Articles →
                </span>
              </Link>
            </div>
          </div>
        </section>

        {/* Newsletter CTA Section */}
        <section className="py-20 bg-background">
          <div className="max-w-4xl mx-auto px-6 sm:px-8 lg:px-12 text-center">
            <h2 className="font-heading text-4xl md:text-5xl text-foreground mb-6">
              Stay Inspired
            </h2>
            <p className="font-body text-lg text-foreground leading-relaxed mb-8 max-w-2xl mx-auto">
              Join our community and receive weekly nail inspiration, expert tutorials, trend forecasts, and curated product picks delivered directly to your inbox.
            </p>
            <Link 
              href="/subscribe"
              className="inline-block bg-foreground text-background px-8 py-4 font-ui text-sm uppercase tracking-wider hover:opacity-90 transition-opacity"
            >
              Subscribe to Newsletter
            </Link>
          </div>
        </section>

        {/* Collaboration CTA */}
        <section className="py-20 bg-background border-t border-foreground/10">
          <div className="max-w-4xl mx-auto px-6 sm:px-8 lg:px-12 text-center">
            <h2 className="font-heading text-3xl md:text-4xl text-foreground mb-6">
              Collaborate With Mirellé
            </h2>
            <p className="font-body text-base text-foreground leading-relaxed mb-8 max-w-2xl mx-auto">
              Are you a nail salon owner, independent artist, or beauty brand? Explore partnership opportunities to reach our engaged community of 50,000+ monthly readers and 1 million weekly Pinterest viewers.
            </p>
            <Link 
              href="/work-with-us"
              className="font-ui text-sm text-foreground uppercase tracking-wide underline hover:opacity-70 transition-opacity"
            >
              Learn About Partnerships
              
            </Link>
          </div>
        </section>
      </div>
    </>
  );
}
