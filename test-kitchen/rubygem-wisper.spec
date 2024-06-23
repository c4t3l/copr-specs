# Generated from wisper-2.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name wisper

Name: rubygem-%{gem_name}
Version: 2.0.1
Release: 1%{?dist}
Summary: A micro library providing objects with Publish-Subscribe capabilities
License: MIT
URL: https://github.com/krisleech/wisper
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
A micro library providing objects with Publish-Subscribe capabilities.
Both synchronous (in-process) and asynchronous (out-of-process) subscriptions
are supported.
Check out the Wiki for articles, guides and examples:
https://github.com/krisleech/wisper/wiki.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%{_bindir}/console
%{_bindir}/setup
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%{gem_instdir}/bin
%{gem_instdir}/gem-public_cert.pem
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/wisper.gemspec

%changelog
* Sat Sep 17 2022 Robby Callicotte <rcallicotte@fedoraproject.org> - 2.0.1-1
- Initial package
