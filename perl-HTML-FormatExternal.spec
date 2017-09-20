#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	FormatExternal
%include	/usr/lib/rpm/macros.perl
Summary:	HTML::FormatExternal - HTML to text formatting using external programs
Summary(pl.UTF-8):	HTML::FormatExternal - formatowanie HTML-a do tekstu przy użyciu programów zewnętrznych
Name:		perl-HTML-FormatExternal
Version:	26
Release:	1
License:	GPL v3+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	94ad331e344440306cd821b0260ddb4f
URL:		http://search.cpan.org/dist/HTML-FormatExternal/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IPC-Run
BuildRequires:	perl-URI >= 0.08
BuildRequires:	perl-constant-defer
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a collection of formatter modules turning HTML into plain text
by dumping it through the respective external programs.

HTML::FormatText::Elinks HTML::FormatText::Html2text
HTML::FormatText::Links HTML::FormatText::Lynx
HTML::FormatText::Netrik HTML::FormatText::Vilistextum
HTML::FormatText::W3m HTML::FormatText::Zen

The module interfaces are compatible with HTML::Formatter modules such
as HTML::FormatText, but the external programs do all the work.

Common formatting options are used where possible, such as leftmargin
and rightmargin. So just by switching the class you can use a
different program (or the plain HTML::FormatText) according to
personal preference, or strengths and weaknesses, or what you've got.

There's nothing particularly difficult about piping through these
programs, but a unified interface hides details like how to set
margins and how to force input or output charsets.

%description -l pl.UTF-8
Ten pakiet zawiera zbiór modułów formatujących zamieniających HTML na
zwykły tekst poprzez zrzucanie go przez odpowiednie programy
zewnętrzne.

HTML::FormatText::Elinks HTML::FormatText::Html2text
HTML::FormatText::Links HTML::FormatText::Lynx
HTML::FormatText::Netrik HTML::FormatText::Vilistextum
HTML::FormatText::W3m HTML::FormatText::Zen

Interfejsy modułów są zgodne z modułami HTML::Formatter, takimi jak
HTML::FormatText, ale cała praca wykonywana jest przez zewnętrzne
programy.

W miarę możliwości używane są wspólne opcje formatowania, takie jak
marginesy (leftmargin i rightmargin). Poprzez proste przełączenie
klasy można używać innego programu (lub zwykłego HTML::FormatText)
według własnych preferencji, zalet i wad, albo posiadanych programów.

Nie ma nic trudnego w przepuszczaniu potoków przez te programy, ale
ujednolicony interfejs ukrywa szczegóły, takie jak sposób ustawiania
marginesów, albo wymuszania wejściowego lub wyjściowego zestawu
znaków.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTML/FormatExternal.pm
# XXX: shared with perl-HTML-FormatText-WithLinks
%dir %{perl_vendorlib}/HTML/FormatText
%{perl_vendorlib}/HTML/FormatText/Elinks.pm
%{perl_vendorlib}/HTML/FormatText/Html2text.pm
%{perl_vendorlib}/HTML/FormatText/Links.pm
%{perl_vendorlib}/HTML/FormatText/Lynx.pm
%{perl_vendorlib}/HTML/FormatText/Netrik.pm
%{perl_vendorlib}/HTML/FormatText/Vilistextum.pm
%{perl_vendorlib}/HTML/FormatText/W3m.pm
%{perl_vendorlib}/HTML/FormatText/Zen.pm
%{_mandir}/man3/HTML::FormatExternal.3pm*
%{_mandir}/man3/HTML::FormatText::*.3pm*
%{_examplesdir}/%{name}-%{version}
