// src/components/Inspo/InspoClient.tsx
'use client';

import { useState, useRef, useEffect } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import Breadcrumbs from '@/components/Breadcrumbs';
import type { DesignData, DesignImage } from '@/types/inspo';

interface InspoClientProps {
  designData: DesignData;
  initialImages: DesignImage[];
  relatedDesigns: DesignData[];
  breadcrumbItems: Array<{ label: string; href: string }>;
}

export default function InspoClient({
  designData,
  initialImages,
  relatedDesigns,
  breadcrumbItems,
}: InspoClientProps) {
  const [selectedImage, setSelectedImage] = useState<DesignImage | null>(null);
  const [filter, setFilter] = useState<'all' | 'premium'>('all');
  const [sortBy, setSortBy] = useState<'trending' | 'newest' | 'popular'>('trending');
  const [displayCount, setDisplayCount] = useState(20);
  const [likedImages, setLikedImages] = useState<Set<string>>(new Set());
  const [savedImages, setSavedImages] = useState<Set<string>>(new Set());
  const [aboutOpen, setAboutOpen] = useState(false);
  const [tipsOpen, setTipsOpen] = useState(false);
  const loadMoreRef = useRef<HTMLDivElement>(null);

  // Filter images
  const filteredImages = filter === 'premium' 
    ? initialImages.filter(img => img.isPremium)
    : initialImages;

  // Sort images
  const sortedImages = [...filteredImages].sort((a, b) => {
    if (sortBy === 'popular') {
      return (likedImages.has(b.id) ? 1 : 0) - (likedImages.has(a.id) ? 1 : 0);
    }
    return 0; // trending and newest stay in original order
  });

  // Paginated images
  const displayedImages = sortedImages.slice(0, displayCount);
  const hasMore = displayCount < sortedImages.length;

  // Infinite scroll
  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting && hasMore) {
          setDisplayCount(prev => prev + 20);
        }
      },
      { threshold: 0.1 }
    );

    if (loadMoreRef.current) {
      observer.observe(loadMoreRef.current);
    }

    return () => observer.disconnect();
  }, [hasMore]);
  // 🎯 ADD THESE HANDLERS AFTER YOUR OTHER useEffect HOOKS (around line ~70)

// Keyboard Navigation for Lightbox
useEffect(() => {
  if (!selectedImage) return;

  const handleKeyPress = (e: KeyboardEvent) => {
    if (e.key === 'Escape') {
      setSelectedImage(null);
    } else if (e.key === 'ArrowLeft') {
      // Previous image
      const currentIndex = displayedImages.findIndex(img => img.id === selectedImage.id);
      const prevIndex = currentIndex > 0 ? currentIndex - 1 : displayedImages.length - 1;
      setSelectedImage(displayedImages[prevIndex]);
    } else if (e.key === 'ArrowRight') {
      // Next image
      const currentIndex = displayedImages.findIndex(img => img.id === selectedImage.id);
      const nextIndex = currentIndex < displayedImages.length - 1 ? currentIndex + 1 : 0;
      setSelectedImage(displayedImages[nextIndex]);
    }
  };

  window.addEventListener('keydown', handleKeyPress);
  
  // Prevent body scroll when lightbox is open
  document.body.style.overflow = 'hidden';

  return () => {
    window.removeEventListener('keydown', handleKeyPress);
    document.body.style.overflow = 'unset';
  };
}, [selectedImage, displayedImages]);

// Touch Gesture Support for Mobile Swipe
useEffect(() => {
  if (!selectedImage) return;

  let touchStartX = 0;
  let touchEndX = 0;

  const handleTouchStart = (e: TouchEvent) => {
    touchStartX = e.changedTouches[0].screenX;
  };

  const handleTouchEnd = (e: TouchEvent) => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  };

  const handleSwipe = () => {
    const swipeThreshold = 50; // minimum distance for swipe

    if (touchStartX - touchEndX > swipeThreshold) {
      // Swiped left - show next image
      const currentIndex = displayedImages.findIndex(img => img.id === selectedImage.id);
      const nextIndex = currentIndex < displayedImages.length - 1 ? currentIndex + 1 : 0;
      setSelectedImage(displayedImages[nextIndex]);
    }

    if (touchEndX - touchStartX > swipeThreshold) {
      // Swiped right - show previous image
      const currentIndex = displayedImages.findIndex(img => img.id === selectedImage.id);
      const prevIndex = currentIndex > 0 ? currentIndex - 1 : displayedImages.length - 1;
      setSelectedImage(displayedImages[prevIndex]);
    }
  };

  window.addEventListener('touchstart', handleTouchStart);
  window.addEventListener('touchend', handleTouchEnd);

  return () => {
    window.removeEventListener('touchstart', handleTouchStart);
    window.removeEventListener('touchend', handleTouchEnd);
  };
}, [selectedImage, displayedImages]);

  // Like/Save handlers
  const handleLike = (imageId: string) => {
    setLikedImages(prev => {
      const newSet = new Set(prev);
      if (newSet.has(imageId)) {
        newSet.delete(imageId);
      } else {
        newSet.add(imageId);
      }
      return newSet;
    });
  };

  const handleSave = (imageId: string) => {
    setSavedImages(prev => {
      const newSet = new Set(prev);
      if (newSet.has(imageId)) {
        newSet.delete(imageId);
      } else {
        newSet.add(imageId);
      }
      return newSet;
    });
  };

  const handleShare = async () => {
    if (navigator.share) {
      try {
        await navigator.share({
          title: designData.displayName,
          text: designData.description,
          url: window.location.href,
        });
      } catch (err) {
        console.log('Share cancelled');
      }
    } else {
      navigator.clipboard.writeText(window.location.href);
      alert('Link copied to clipboard!');
    }
  };


  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-cyan-50">
      {/* Breadcrumbs */}
      <div className="bg-white border-b border-gray-200 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <Breadcrumbs items={breadcrumbItems} currentPage={designData.displayName} />
        </div>
      </div>
  
      {/* Hero Section */}
      <section className="relative overflow-hidden">
        <div className="relative h-[60vh] md:h-[70vh] min-h-[500px]">
          {designData.heroImage.startsWith('/') ? (
            <Image
              src={designData.heroImage}
              alt={`${designData.displayName} winter nail designs 2025 inspiration`}
              fill
              priority
              className="object-cover"
              sizes="100vw"
            />
          ) : (
            <div
              className="absolute inset-0 bg-cover bg-center"
              style={{ backgroundImage: `url(${designData.heroImage})` }}
            />
          )}
          
          <div className="absolute inset-0 bg-gradient-to-b from-black/70 via-black/50 to-black/80" />
          
          <div className="relative h-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col justify-center text-white">
            <div className="inline-flex w-fit items-center gap-2 bg-white/10 backdrop-blur-md border border-white/30 px-5 py-2 mb-6 text-sm font-semibold uppercase tracking-wider rounded-full">
              <span>{designData.category}</span>
              <span>•</span>
              <span>{designData.year}</span>
            </div>
            
            <h1 className="font-display text-5xl md:text-6xl lg:text-7xl font-bold mb-6 tracking-tight">
              {designData.displayName}
            </h1>
            
            <p className="text-xl md:text-2xl text-white/90 mb-8 max-w-3xl font-light">
              {designData.description}
            </p>

            <div className="flex gap-4 mb-8 text-4xl">
              {designData.emojis.map((emoji, i) => (
                <span key={i} className="animate-bounce" style={{ animationDelay: `${i * 0.1}s` }}>
                  {emoji}
                </span>
              ))}
            </div>

            {designData.tldr && (
              <div className="bg-white/10 backdrop-blur-md border border-white/20 rounded-2xl p-6 max-w-2xl">
                <h3 className="text-lg font-semibold mb-4 text-white flex items-center gap-2">
                  <span className="text-2xl">✨</span>
                  Quick Overview
                </h3>
                <ul className="space-y-3 text-white/90">
                  {designData.tldr.summary.map((item, i) => (
                    <li key={i} className="flex items-start gap-3">
                      <span className="text-cyan-300 mt-1 flex-shrink-0">✓</span>
                      <span className="text-sm md:text-base">{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>

        <div className="absolute bottom-0 left-0 right-0">
          <svg className="w-full h-12 fill-white" viewBox="0 0 1200 120" preserveAspectRatio="none">
            <path d="M321.39,56.44c58-10.79,114.16-30.13,172-41.86,82.39-16.72,168.19-17.73,250.45-.39C823.78,31,906.67,72,985.66,92.83c70.05,18.48,146.53,26.09,214.34,3V0H0V27.35A600.21,600.21,0,0,0,321.39,56.44Z" />
          </svg>
        </div>
      </section>

      {/* Sticky Action Bar */}
      <section className="bg-white border-b border-gray-200 sticky top-0 z-40 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
          <div className="flex items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <button
                onClick={() => handleLike('category')}
                className="flex items-center gap-2 px-4 py-2 bg-white border-2 border-gray-200 rounded-full font-medium hover:border-pink-400 hover:text-pink-600 transition-all"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
                <span className="hidden sm:inline">Like</span>
              </button>
              
              <button
                onClick={() => handleSave('category')}
                className="flex items-center gap-2 px-4 py-2 bg-white border-2 border-gray-200 rounded-full font-medium hover:border-burgundy-400 hover:text-burgundy-600 transition-all"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
                </svg>
                <span className="hidden sm:inline">Save</span>
              </button>

              <button
                onClick={handleShare}
                className="flex items-center gap-2 px-4 py-2 bg-white border-2 border-gray-200 rounded-full font-medium hover:border-blue-400 hover:text-blue-600 transition-all"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m0 2.684l6.632 3.316m-6.632-6l6.632-3.316m0 0a3 3 0 105.367-2.684 3 3 0 00-5.367 2.684zm0 9.316a3 3 0 105.368 2.684 3 3 0 00-5.368-2.684z" />
                </svg>
                <span className="hidden sm:inline">Share</span>
              </button>
            </div>

            <div className="text-sm text-gray-600 font-medium">
              {displayedImages.length} of {sortedImages.length} designs
            </div>
          </div>
        </div>
      </section>

      {/* Filter & Sort Bar */}
      <section className="bg-white border-b border-gray-200 py-4">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
            <div className="flex flex-wrap gap-3">
              <button
                onClick={() => setFilter('all')}
                className={`px-5 py-2 rounded-full font-medium transition-all duration-300 ${
                  filter === 'all'
                    ? 'bg-burgundy-700 text-white shadow-burgundy'
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
              >
                All ({initialImages.length})
              </button>
              <button
                onClick={() => setFilter('premium')}
                className={`px-5 py-2 rounded-full font-medium transition-all duration-300 inline-flex items-center gap-2 ${
                  filter === 'premium'
                    ? 'bg-burgundy-700 text-white shadow-burgundy'
                    : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                }`}
              >
                <span className="text-yellow-500">⭐</span>
                Premium ({initialImages.filter(img => img.isPremium).length})
              </button>
            </div>
            
            <select 
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value as any)}
              className="px-4 py-2 border border-gray-300 rounded-full text-sm font-medium focus:ring-2 focus:ring-burgundy-500 focus:border-transparent cursor-pointer bg-white"
            >
              <option value="trending">🔥 Trending</option>
              <option value="newest">🆕 Newest</option>
              <option value="popular">💖 Most Liked</option>
            </select>
          </div>
        </div>
      </section>

      {/* Masonry Gallery Grid */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {displayedImages.length === 0 ? (
          <div className="text-center py-20">
            <div className="text-6xl mb-4">🎨</div>
            <h3 className="text-2xl font-bold text-gray-900 mb-2">
              No designs available yet
            </h3>
            <p className="text-gray-500 text-lg mb-6">
              We're adding amazing {designData.displayName.toLowerCase()} soon!
            </p>
            <Link 
              href="/inspo"
              className="inline-flex items-center gap-2 bg-burgundy-700 text-white px-6 py-3 rounded-full font-semibold hover:bg-burgundy-800 transition-colors"
            >
              Browse All Categories
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
              </svg>
            </Link>
          </div>
        ) : (
          <>
            {/* Masonry CSS Grid */}
            <div className="columns-2 md:columns-3 lg:columns-4 gap-4 space-y-4">
              {displayedImages.map((image) => (
                <div
                  key={image.id}
                  className="break-inside-avoid mb-4"
                >
                  <div className="group relative overflow-hidden rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-300 bg-white">
                    <button
                      onClick={() => setSelectedImage(image)}
                      className="w-full"
                    >
                      <div className="relative">
                        <Image
                          src={image.url}
                          alt={image.alt}
                          width={400}
                          height={600}
                          className="w-full h-auto object-cover transform group-hover:scale-105 transition-transform duration-500"
                          sizes="(max-width: 768px) 50vw, (max-width: 1200px) 33vw, 25vw"
                        />
                        
                        {/* Hover Overlay */}
                        <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/40 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                          <div className="absolute bottom-0 left-0 right-0 p-4">
                            <p className="text-white text-sm font-medium line-clamp-3">
                              {image.alt}
                            </p>
                          </div>
                        </div>

                        {/* Premium Badge */}
                        {image.isPremium && (
                          <div className="absolute top-3 right-3 bg-gradient-to-r from-yellow-400 to-orange-400 text-yellow-900 text-xs font-bold px-3 py-1.5 rounded-full shadow-lg">
                            ⭐ PRO
                          </div>
                        )}

                        {/* View Button */}
                        <div className="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                          <span className="bg-white text-burgundy-700 px-4 py-2 rounded-full text-sm font-bold shadow-lg">
                            View Full
                          </span>
                        </div>
                      </div>
                    </button>

                    {/* Like/Save Actions */}
                    <div className="flex items-center justify-between p-3 bg-white">
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          handleLike(image.id);
                        }}
                        className={`flex items-center gap-1 text-sm font-medium transition-colors ${
                          likedImages.has(image.id) ? 'text-pink-600' : 'text-gray-600 hover:text-pink-600'
                        }`}
                      >
                        <svg className={`w-5 h-5 ${likedImages.has(image.id) ? 'fill-current' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                        </svg>
                      </button>

                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          handleSave(image.id);
                        }}
                        className={`flex items-center gap-1 text-sm font-medium transition-colors ${
                          savedImages.has(image.id) ? 'text-burgundy-600' : 'text-gray-600 hover:text-burgundy-600'
                        }`}
                      >
                        <svg className={`w-5 h-5 ${savedImages.has(image.id) ? 'fill-current' : ''}`} fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
                        </svg>
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>

            {/* Load More Trigger */}
            {hasMore && (
              <div ref={loadMoreRef} className="py-12 text-center">
                <div className="inline-flex items-center gap-2 text-gray-600">
                  <svg className="animate-spin w-5 h-5" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Loading more designs...
                </div>
              </div>
            )}

            {!hasMore && sortedImages.length > 0 && (
              <div className="text-center py-12">
                <p className="text-gray-600 mb-4">
                  You've seen all {sortedImages.length} designs! 🎉
                </p>
                <button 
                  onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
                  className="inline-flex items-center gap-2 px-6 py-3 bg-gray-200 text-gray-700 rounded-full font-semibold hover:bg-gray-300 transition-colors"
                >
                  Back to Top ↑
                </button>
              </div>
            )}
          </>
        )}
      </section>

      {/* About This Style (Collapsible) */}
      <section className="py-16 bg-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <details 
            open={aboutOpen}
            onToggle={(e: any) => setAboutOpen(e.target.open)}
            className="group bg-gradient-to-br from-slate-50 to-blue-50 rounded-3xl shadow-lg overflow-hidden border border-gray-100"
          >
            <summary className="cursor-pointer px-8 py-6 flex justify-between items-center hover:bg-white/50 transition-colors touch-target">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 bg-burgundy-100 rounded-xl flex items-center justify-center">
                  <span className="text-2xl">💡</span>
                </div>
                <div>
                  <h2 className="font-display text-2xl font-bold text-gray-900">
                    About {designData.displayName}
                  </h2>
                  <p className="text-sm text-gray-600">
                    Everything you need to know about this style
                  </p>
                </div>
              </div>
              
              <svg className="w-6 h-6 text-burgundy-600 transform group-open:rotate-180 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </summary>
            
            <div className="px-8 pb-8 space-y-6 text-gray-700 leading-relaxed">
              <div className="prose prose-lg max-w-none">
                <p className="text-lg font-medium text-gray-900 mb-4">
                  {designData.description}
                </p>
                
                <p className="mb-4">
                  {designData.displayName} are trending for winter 2025, combining timeless elegance with modern nail art techniques. 
                  This style works beautifully on all nail lengths and shapes, making it perfect for both everyday wear and special occasions.
                </p>

                <h3 className="font-display text-xl font-bold text-gray-900 mt-6 mb-3">
                  Key Characteristics
                </h3>
                <ul className="space-y-2">
                  <li className="flex items-start gap-2">
                    <span className="text-burgundy-600 mt-1">✓</span>
                    <span>Versatile design that complements all skin tones and nail shapes</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-burgundy-600 mt-1">✓</span>
                    <span>Professional appearance suitable for work and formal events</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-burgundy-600 mt-1">✓</span>
                    <span>Long-lasting finish when applied with gel or dip powder</span>
                  </li>
                  <li className="flex items-start gap-2">
                    <span className="text-burgundy-600 mt-1">✓</span>
                    <span>Easy to customize with different colors, textures, and embellishments</span>
                  </li>
                </ul>

                <h3 className="font-display text-xl font-bold text-gray-900 mt-6 mb-3">
                  Perfect For
                </h3>
                <p>
                  {designData.displayName} are ideal for {designData.perfectFor?.join(', ').toLowerCase() || 'any occasion'}.
                  Whether you're attending a winter wedding, holiday party, or simply want elegant everyday nails,
                  this style delivers sophisticated results that last.
                </p>
              </div>
            </div>
          </details>
        </div>
      </section>

      {/* Design Tips Section */}
      {designData.styleGuide && designData.styleGuide.length > 0 && (
        <section className="py-16 bg-gradient-to-br from-slate-50 to-blue-50">
          <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div className="text-center mb-12">
              <h2 className="text-4xl font-display font-bold text-gray-900 mb-4">
                Pro Tips for {designData.displayName}
              </h2>
              <p className="text-xl text-gray-600">
                Expert advice to achieve the perfect look
              </p>
            </div>
            
            <div className="grid md:grid-cols-3 gap-6">
              {designData.styleGuide.map((tip, index) => (
                <div key={index} className="bg-white rounded-2xl p-6 shadow-lg border border-gray-100 hover:shadow-xl transition-shadow">
                  <div className="w-14 h-14 bg-gradient-to-br from-burgundy-100 to-pink-100 rounded-xl flex items-center justify-center mb-4">
                    <span className="text-3xl">{['💡', '✨', '🎨', '💅', '🌟', '⭐'][index % 6]}</span>
                  </div>
                  
                  <h3 className="font-bold text-lg text-gray-900 mb-2">
                    Tip #{index + 1}
                  </h3>
                  
                  <p className="text-gray-600 leading-relaxed">
                    {tip}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Perfect For Section */}
      {designData.perfectFor && designData.perfectFor.length > 0 && (
        <section className="bg-white py-16">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 className="text-3xl font-display font-bold text-gray-900 mb-8 text-center">
              Perfect For
            </h2>
            <div className="flex flex-wrap gap-3 justify-center">
              {designData.perfectFor.map((item, i) => (
                <span
                  key={i}
                  className="bg-gradient-to-r from-burgundy-50 to-pink-50 border border-burgundy-200 text-burgundy-800 px-5 py-3 rounded-full text-sm font-semibold shadow-sm"
                >
                  {item}
                </span>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* FAQ Section */}
      <section className="py-16 bg-gradient-to-b from-cream-50 to-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-4xl font-display font-bold text-gray-900 mb-4">
              Frequently Asked Questions
            </h2>
            <p className="text-xl text-gray-600">
              Common questions about {designData.displayName.toLowerCase()}
            </p>
          </div>
          
          <div className="space-y-4">
            {[
              {
                q: `What nail shapes work best for ${designData.displayName.toLowerCase()}?`,
                a: `Almond, oval, and square shapes showcase ${designData.displayName.toLowerCase()} beautifully. Almond and oval shapes elongate fingers, while square provides a classic, clean look. Choose based on your natural nail shape and lifestyle preferences.`
              },
              {
                q: `How long do ${designData.displayName.toLowerCase()} last?`,
                a: `With proper application using gel polish, ${designData.displayName.toLowerCase()} typically last 2-3 weeks. Regular polish lasts 5-7 days. Using a quality base coat, top coat, and avoiding harsh chemicals helps extend wear time significantly.`
              },
              {
                q: `Can I create ${designData.displayName.toLowerCase()} at home?`,
                a: `Yes! ${designData.displayName.toLowerCase()} can be achieved at home with the right tools and practice. Start with simpler designs and work your way up to more complex techniques. Quality nail tools and steady hands are key to success.`
              },
              {
                q: `What's the best way to maintain ${designData.displayName.toLowerCase()}?`,
                a: `Apply cuticle oil daily, wear gloves when doing dishes or cleaning, avoid using nails as tools, and touch up the top coat every 3-4 days. Keep nails hydrated and protected from harsh chemicals for best results.`
              },
              {
                q: `How much does it cost to get ${designData.displayName.toLowerCase()} at a salon?`,
                a: `Salon prices for ${designData.displayName.toLowerCase()} typically range from $40-80 for basic designs with regular polish, $60-100 for gel, and $80-150+ for intricate nail art with embellishments. Prices vary by location and salon expertise.`
              }
            ].map((faq, index) => (
              <details key={index} className="group bg-white rounded-2xl border border-gray-200 overflow-hidden hover:border-burgundy-300 transition-colors shadow-sm">
                <summary className="cursor-pointer px-6 py-5 flex justify-between items-center touch-target">
                  <h3 className="font-semibold text-gray-900 pr-4 text-lg">
                    {faq.q}
                  </h3>
                  <svg className="w-5 h-5 text-burgundy-600 transform group-open:rotate-45 transition-transform flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                  </svg>
                </summary>
                
                <div className="px-6 pb-5 text-gray-600 leading-relaxed">
                  <p>{faq.a}</p>
                </div>
              </details>
            ))}
          </div>
        </div>
      </section>

      {/* Related Designs */}
      {relatedDesigns.length > 0 && (
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <h2 className="text-4xl font-display font-bold text-gray-900 mb-12 text-center">
            You Might Also Love
          </h2>
          
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {relatedDesigns.map((design) => (
              <Link
                key={design.slug}
                href={`/inspo/${design.slug}`}
                className="group relative bg-white rounded-3xl shadow-lg hover:shadow-2xl transition-all duration-500 overflow-hidden"
              >
                <div className="relative h-80 overflow-hidden">
                  {design.heroImage.startsWith('/') ? (
                    <Image
                      src={design.heroImage}
                      alt={`${design.displayName} nail design inspiration`}
                      fill
                      className="object-cover transform group-hover:scale-110 transition-transform duration-700"
                      sizes="(max-width: 768px) 100vw, 33vw"
                    />
                  ) : (
                    <div
                      className="absolute inset-0 bg-cover bg-center transform group-hover:scale-110 transition-transform duration-700"
                      style={{ backgroundImage: `url(${design.heroImage})` }}
                    />
                  )}
                  <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent" />
                  
                  <div className="absolute bottom-0 left-0 right-0 p-6 text-white">
                    <span className="inline-block px-3 py-1 bg-white/20 backdrop-blur-sm rounded-full text-xs font-semibold uppercase mb-3">
                      {design.category}
                    </span>
                    <h3 className="text-2xl font-display font-bold mb-2 group-hover:text-cyan-300 transition-colors">
                      {design.displayName}
                    </h3>
                    <p className="text-white/90 text-sm mb-3 line-clamp-2">
                      {design.description}
                    </p>
                    <span className="inline-flex items-center text-sm font-semibold border-b-2 border-transparent group-hover:border-cyan-300 transition-all">
                      View Gallery →
                    </span>
                  </div>
                </div>
              </Link>
            ))}
          </div>
        </section>
      )}
{selectedImage && (
  <div
    className="fixed inset-0 bg-black/98 backdrop-blur-xl z-[100] flex items-center justify-center"
    onClick={() => setSelectedImage(null)}
    style={{ animation: 'fadeIn 0.3s ease-out' }}
  >
    {/* Close Button - Top Right */}
    <button
      className="fixed top-6 right-6 z-[110] group"
      onClick={() => setSelectedImage(null)}
      aria-label="Close lightbox"
    >
      <div className="w-14 h-14 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center hover:bg-white/20 transition-all duration-300 shadow-2xl">
        <svg className="w-6 h-6 text-white group-hover:rotate-90 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
        </svg>
      </div>
    </button>

    {/* Navigation Buttons */}
    {displayedImages.length > 1 && (
      <>
        {/* Previous Button */}
        <button
          className="fixed left-6 top-1/2 -translate-y-1/2 z-[110] group"
          onClick={(e) => {
            e.stopPropagation();
            const currentIndex = displayedImages.findIndex(img => img.id === selectedImage.id);
            const prevIndex = currentIndex > 0 ? currentIndex - 1 : displayedImages.length - 1;
            setSelectedImage(displayedImages[prevIndex]);
          }}
          aria-label="Previous image"
        >
          <div className="w-14 h-14 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center hover:bg-white/20 hover:scale-110 transition-all duration-300 shadow-2xl">
            <svg className="w-6 h-6 text-white group-hover:-translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
            </svg>
          </div>
        </button>

        {/* Next Button */}
        <button
          className="fixed right-6 top-1/2 -translate-y-1/2 z-[110] group"
          onClick={(e) => {
            e.stopPropagation();
            const currentIndex = displayedImages.findIndex(img => img.id === selectedImage.id);
            const nextIndex = currentIndex < displayedImages.length - 1 ? currentIndex + 1 : 0;
            setSelectedImage(displayedImages[nextIndex]);
          }}
          aria-label="Next image"
        >
          <div className="w-14 h-14 rounded-full bg-white/10 backdrop-blur-md border border-white/20 flex items-center justify-center hover:bg-white/20 hover:scale-110 transition-all duration-300 shadow-2xl">
            <svg className="w-6 h-6 text-white group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </div>
        </button>
      </>
    )}

    {/* Main Content Container */}
    <div 
      className="relative w-full h-full flex flex-col items-center justify-center p-4 md:p-8"
      onClick={(e) => e.stopPropagation()}
    >
      {/* Image Container - Perfect Fit */}
      <div className="relative max-w-7xl max-h-[85vh] w-full flex items-center justify-center mb-4">
        <Image
          src={selectedImage.url}
          alt={selectedImage.alt}
          width={1920}
          height={1280}
          className="max-h-[85vh] w-auto max-w-full object-contain rounded-2xl shadow-2xl"
          style={{ animation: 'scaleIn 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)' }}
          priority
        />
      </div>

      {/* Glassmorphic Info Panel */}
      <div className="w-full max-w-4xl bg-white/10 backdrop-blur-2xl border border-white/20 rounded-3xl p-6 md:p-8 shadow-2xl">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
          {/* Left Side - Description */}
          <div className="flex-1">
            <p className="text-white text-lg md:text-xl font-medium leading-relaxed mb-4">
              {selectedImage.alt}
            </p>
            
            {/* Image Counter */}
            <div className="flex items-center gap-3 text-white/70 text-sm">
              <span className="inline-flex items-center gap-2 bg-white/10 px-4 py-2 rounded-full backdrop-blur-sm">
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
                {displayedImages.findIndex(img => img.id === selectedImage.id) + 1} / {displayedImages.length}
              </span>
              
              {selectedImage.isPremium && (
                <span className="inline-flex items-center gap-1.5 bg-gradient-to-r from-yellow-400/20 to-orange-400/20 border border-yellow-400/30 px-4 py-2 rounded-full backdrop-blur-sm">
                  <span className="text-yellow-300">⭐</span>
                  <span className="text-yellow-200 font-semibold">Premium</span>
                </span>
              )}
            </div>
          </div>

          {/* Right Side - Action Buttons */}
          <div className="flex items-center gap-3">
            {/* Like Button */}
            <button
              onClick={(e) => {
                e.stopPropagation();
                handleLike(selectedImage.id);
              }}
              className={`group relative overflow-hidden px-6 py-3 rounded-full font-semibold transition-all duration-300 shadow-xl ${
                likedImages.has(selectedImage.id)
                  ? 'bg-gradient-to-r from-pink-500 to-rose-500 text-white scale-105'
                  : 'bg-white/10 backdrop-blur-md border border-white/20 text-white hover:bg-white/20 hover:scale-105'
              }`}
            >
              <span className="relative z-10 flex items-center gap-2">
                <svg 
                  className={`w-5 h-5 transition-transform ${likedImages.has(selectedImage.id) ? 'scale-110' : 'group-hover:scale-110'}`} 
                  fill={likedImages.has(selectedImage.id) ? 'currentColor' : 'none'} 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
                {likedImages.has(selectedImage.id) ? 'Liked' : 'Like'}
              </span>
            </button>

            {/* Save Button */}
            <button
              onClick={(e) => {
                e.stopPropagation();
                handleSave(selectedImage.id);
              }}
              className={`group relative overflow-hidden px-6 py-3 rounded-full font-semibold transition-all duration-300 shadow-xl ${
                savedImages.has(selectedImage.id)
                  ? 'bg-gradient-to-r from-burgundy-600 to-purple-600 text-white scale-105'
                  : 'bg-white/10 backdrop-blur-md border border-white/20 text-white hover:bg-white/20 hover:scale-105'
              }`}
            >
              <span className="relative z-10 flex items-center gap-2">
                <svg 
                  className={`w-5 h-5 transition-transform ${savedImages.has(selectedImage.id) ? 'scale-110' : 'group-hover:scale-110'}`} 
                  fill={savedImages.has(selectedImage.id) ? 'currentColor' : 'none'} 
                  stroke="currentColor" 
                  viewBox="0 0 24 24"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z" />
                </svg>
                {savedImages.has(selectedImage.id) ? 'Saved' : 'Save'}
              </span>
            </button>

            {/* Pinterest Link */}
            {selectedImage.pinterestUrl && (
              <a
                href={selectedImage.pinterestUrl}
                target="_blank"
                rel="noopener noreferrer"
                onClick={(e) => e.stopPropagation()}
                className="group px-6 py-3 rounded-full font-semibold bg-white/10 backdrop-blur-md border border-white/20 text-white hover:bg-white/20 hover:scale-105 transition-all duration-300 shadow-xl"
              >
                <span className="flex items-center gap-2">
                  <svg className="w-5 h-5 group-hover:scale-110 transition-transform" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 0C5.373 0 0 5.372 0 12c0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738.098.119.112.224.083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.163 0 7.398 2.967 7.398 6.931 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.631-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24 12 24c6.627 0 12-5.373 12-12 0-6.628-5.373-12-12-12z"/>
                  </svg>
                  Pin
                </span>
              </a>
            )}
          </div>
        </div>

        {/* Keyboard Hint */}
        <div className="mt-6 pt-6 border-t border-white/10 flex items-center justify-center gap-6 text-white/60 text-sm">
          <span className="flex items-center gap-2">
            <kbd className="px-2 py-1 bg-white/10 rounded text-xs">←</kbd>
            <kbd className="px-2 py-1 bg-white/10 rounded text-xs">→</kbd>
            Navigate
          </span>
          <span className="flex items-center gap-2">
            <kbd className="px-3 py-1 bg-white/10 rounded text-xs">ESC</kbd>
            Close
          </span>
        </div>
      </div>
    </div>

    {/* Animations CSS - Add to your global CSS or component styles */}
    <style jsx>{`
      @keyframes fadeIn {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      @keyframes scaleIn {
        from {
          opacity: 0;
          transform: scale(0.9);
        }
        to {
          opacity: 1;
          transform: scale(1);
        }
      }
    `}</style>
    </div>
  );
}
